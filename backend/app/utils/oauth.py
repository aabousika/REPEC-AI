import os
from flask import flash, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import current_user, login_user
from app.models.user import User
from app import db



def init_oauth(app):
# الحصول على CLIENT_ID و CLIENT_SECRET من المتغيرات البيئية

    google_bp = make_google_blueprint(
        client_id=os.environ.get('GOOGLE_CLIENT_ID'),
        client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
        scope=['openid', 'https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email'],
        redirect_to='auth.google_login_callback'
    )
    
    app.register_blueprint(google_bp, url_prefix='/login')

# التحقق من وجود المتغيرات البيئية
    if os.environ.get('FLASK_ENV') == 'production':
        app.config['PREFERRED_URL_SCHEME'] = 'https'
       



# التسجيل مع جوجل باستخدام oauth
def handle_google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    
    resp = google.get('/oauth2/v2/userinfo')
    if not resp.ok:
        flash('Failed to get user info from Google.', 'danger')
        return redirect(url_for('auth.login'))
    
    google_info = resp.json()
    google_id = google_info['id']
    email = google_info['email']
    
    user = User.query.filter_by(google_id=google_id).first()
    if not user:
        user = User.query.filter_by(email=email).first()
        if user:
            user.google_id = google_id
            db.session.commit()
        else:
            username = email.split('@')[0]
            base_username = username
            counter = 1
            while User.query.filter_by(username=username).first():
                username = f"{base_username}{counter}"
                counter += 1
            
            user = User(
                username=username,
                email=email,
                google_id=google_id,
                first_name=google_info.get('given_name', ''),
                last_name=google_info.get('family_name', '')
            )
            db.session.add(user)
            db.session.commit()
    
    login_user(user)
    flash('Successfully logged in with Google.', 'success')
    
    next_page = url_for('main.dashboard')
    return redirect(next_page)

    


