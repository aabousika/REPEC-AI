from flask import Blueprint, jsonify, request, current_app
from flask_login import login_required, current_user
from app.models.city import City, Attraction
from app.models.booking import Booking, ChatSession, ChatMessage
from app.models.user import UserPreference
from app.utils.chatgpt import ChatGPTRecommender
from app import db
from datetime import datetime
import uuid

"""
# Blueprint setup
init Blueprint api_bp
"""
api_bp=Blueprint('api',__name__)
recomendation=ChatGPTRecommender()
"""""
# — Chat —
POST /chat:
  require login
  msg = request.message
  session = find_or_create_active_session(user)
  save ChatMessage(session, user, msg)
  context = load_messages(session)
  reply = ChatGPTRecommender.ask(msg, context)
  save ChatMessage(session, assistant, reply)
  return reply
  """""
@api_bp.route("/chat",methods=['POST'])
@login_required
def chat():
    msg=request.json.get("message")
    if not msg:
        return jsonify({"error":"missing message"}),400
    #find create active session (user)
    session=ChatSession.query.filter_by(user_id=current_user.id ,is_active=True).first()
    if not session:
        session = ChatSession(
            id=str(uuid.uuid4()),
            user_id=current_user.id,
            started_at=datetime.utcnow(),
            is_active=True
        )
        db.session.add(session)
        db.session.commit()

    #save chat message (session ,user ,meaage)
    user_msg=ChatMessage(
        session_id=session.id,
        sender='user',
        content=msg,
        timestap=datetime.utcnow()
    )
    db.session.add(user_msg)
    #load context
    messages=ChatMessage.query.filter_by(session_id=session.id).order_by(ChatMessage.timestap).all()
    context=[{"role":m.sender, "content":m.content} for m in messages]
    #reply
    reply=ChatGPTRecommender.ask(msg,context)
    #save ChatMessage(session, assistant, reply)
    assistant_message=ChatMessage(
        session_id=session.id,
        sender="assistant",
        content=reply,
        timestap=datetime.utcnow()
    )
    db.session.add(assistant_message)
    db.session.commit()
    
    return jsonify({"reply":reply})

        
"""""
POST /chat/start:
  require login
  deactivate any active session(user)
  create new session(user)
  return session_id, session_key


POST /chat/message:
  require login
  session = get_session(data.session_id)
  save ChatMessage(session, user, data.message)
  context = load_messages(session)
  if data.preferences:
    (cities, reply) = Recommender.get_city_recs(data.preferences, context)
    save assistant message with recommendation flag
    update UserPreference(user, data.preferences)
    return reply + city list
  else:
    reply = Recommender.ask(data.message, context)
    save assistant message
    return reply
"""
@api_bp.route('/chat/start', methods=['POST'])
@login_required
def start_chat():
    # deactivate any active session(user)
    ChatSession.query.filter_by(user_id=current_user.id, is_active=True).update({'is_active': False})

    # create new session(user)
    session = ChatSession(
        id=str(uuid.uuid4()),
        user_id=current_user.id,
        started_at=datetime.utcnow(),
        is_active=True
    )
    db.session.add(session)
    db.session.commit()

    # return session_id (and optionally session_key if needed)
    return jsonify({"session_id": session.id})

@api_bp.route('/chat/message', methods=['POST'])
@login_required
def chat_message():
    data = request.get_json()
    session_id = data.get("session_id")
    message = data.get("message")
    preferences = data.get("preferences")  # optional

    # session = get_session(data.session_id)
    session = ChatSession.query.get(session_id)
    if not session or session.user_id != current_user.id:
        return jsonify({"error": "Invalid or unauthorized session."}), 403

    # save ChatMessage(session, user, data.message)
    user_msg = ChatMessage(
        session_id=session.id,
        sender="user",
        content=message,
        timestamp=datetime.utcnow()
    )
    db.session.add(user_msg)

    # context = load_messages(session)
    messages = ChatMessage.query.filter_by(session_id=session.id).order_by(ChatMessage.timestamp).all()
    context = [{"role": m.sender, "content": m.content} for m in messages]

    recommender = ChatGPTRecommender()

    if preferences:
        # (cities, reply) = Recommender.get_city_recs(data.preferences, context)
        cities, reply = recommender.get_city_recs(preferences, context)

        # save assistant message with recommendation flag
        assistant_msg = ChatMessage(
            session_id=session.id,
            sender="assistant",
            content=reply,
            is_recommendation=True,  # تحتاج حقل is_recommendation في النموذج
            timestamp=datetime.utcnow()
        )
        db.session.add(assistant_msg)

        # update UserPreference(user, data.preferences)
        pref = UserPreference.query.filter_by(user_id=current_user.id).first()
        if not pref:
            pref = UserPreference(user_id=current_user.id)
            db.session.add(pref)
        pref.update_from_dict(preferences)

        db.session.commit()
        return jsonify({"reply": reply, "cities": [c.to_dict() for c in cities]})
    else:
        # reply = Recommender.ask(data.message, context)
        reply = recommender.ask(message, context)

        # save assistant message
        assistant_msg = ChatMessage(
            session_id=session.id,
            sender="assistant",
            content=reply,
            timestamp=datetime.utcnow()
        )
        db.session.add(assistant_msg)

        db.session.commit()
        return jsonify({"reply": reply})



"""""
# — Cities —
GET /cities:
  filters = pick(season, budget, name)
  cities = City.query.filter(filters)
  return cities as JSON
"""

@api_bp.route('/cities',methods=['GET'])
def get_cities():
    season=request.args.get('season')
    budget=request.args.get('budget')
    name=request.args.get('name')
    filters=[]
    if season:
        filters.append(City.season==season)
    if budget:
        filters.append(City.budget_category==budget)
    if name:
        filters.append(City.name.ilike(f"%{name}%"))        
    cities = City.query.filter(filters).all()
    return jsonify([city.to_dict() for city in cities])

    

""""
GET /cities/<id>:
  city = City.get_or_404(id)
  attractions = Attraction.filter(city_id=id)
  return city + attractions
"""


""""
# — Bookings —
GET /bookings:
  require login
  bookings = Booking.filter(user_id=user)
  return bookings

POST /bookings:
  require login
  validate data(city_id, start, end, travelers)
  days = end – start
  price = daily_rate(city.budget_category) * days * travelers
  booking = Booking.create(user, city_id, start, end, travelers, price)
  return booking.id

GET /bookings/<id>:
  require login
  booking = Booking.get_or_404(id)
  authorize(user owns booking)
  return booking

PUT /bookings/<id>:
  require login
  booking = Booking.get_or_404(id)
  authorize
  update fields(start, end, travelers, status, notes…)
  if dates or travelers changed:
    recalc price
  save
  return success

DELETE /bookings/<id>:
  require login
  booking = Booking.get_or_404(id)
  authorize
  delete booking
  return success

# — Preferences —
GET /preferences:
  require login
  prefs = UserPreference.get(user) or {}
  return prefs

PUT /preferences:
  require login
  prefs = get_or_create UserPreference(user)
  update prefs from data
  save
  return success

"""