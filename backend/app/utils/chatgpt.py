import os
import openai 
from app.models.city import City
from app import db

openai.api_key = os.environ.get('OPENAI_API_KEY')

class ChatGPTRecommender:
    def __init__(self):
        self.system_prompt = """

"""

        return ...

