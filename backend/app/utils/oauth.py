from app.models.user import User
from app import oauth  
from os import getenv
from dotenv import load_dotenv

# تحميل ملف .env
load_dotenv()


# الحصول على CLIENT_ID و CLIENT_SECRET من المتغيرات البيئية
GOOGLE_CLIENT_ID = getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = getenv("GOOGLE_CLIENT_SECRET")

# التحقق من وجود المتغيرات البيئية
if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
    raise ValueError("CLIENT_ID or CLIENT_SECRET is missing in the .env file")



# التسجيل مع جوجل باستخدام oauth
google = oauth.register(
    name='google',
    GOOGLE_CLIENT_ID=GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET=GOOGLE_CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

    


