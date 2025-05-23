import os
import openai 
from app.models.city import City
from app import db

openai.api_key = os.environ.get('OPENAI_API_KEY')

class ChatGPTRecommender:
    def __init__(self):
        self.system_prompt = """
you are a travel recomended if you need my help to chose best trip for you please answer 

"""
    def get_city_info(self, city_id):
        city = db.session.get(City, city_id)
        if city:
            return f"city :{city.name}\n descripyion:{city.description or 'no description '}"
        return None

    def generate_recommendation(self, city_id):
        city_info = self.get_city_info(city_id)
        if not city_info:
            return "no information "

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"give me a trip with this recomendation \n{city_info}"}
            ]
        )

        return response['choices'][0]['message']['content']

       

