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

# — Cities —
GET /cities:
  filters = pick(season, budget, name)
  cities = City.query.filter(filters)
  return cities as JSON

GET /cities/<id>:
  city = City.get_or_404(id)
  attractions = Attraction.filter(city_id=id)
  return city + attractions

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