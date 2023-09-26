from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import db, User, BaseMedication, ComparisonMedication
import requests


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)


# @app.get('https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=drug_interactions:caffeine&limit=5')
# def index():
#     response = response.json()
#     return response



# url = 'https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=drug_interactions:caffeine&limit=5


# @app.route("/movies")

# def get_movies_list():
#     url = "https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=drug_interactions:caffeine&limit=5"

#     response = urllib.request.urlopen(url)
#     movies = response.read()
#     dict = json.loads(movies)

#     movies = []

#     for movie in dict["results"]:
#         movie = {
#             "title": movie["title"],
#             "overview": movie["overview"],
#         }
        
#         movies.append(movie)

#     return {"results": movies}




# url = "https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=drug_interactions:caffeine&limit=5"
# response = requests.get(url)
# print("status_code", response.status_code)
# response_dict = response.json()
# print(response_dict.keys())


# print(response_dict.get('results'))



new_url = "https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=openfda.generic_name:ketamine"
response2 = requests.get(new_url)
print("status_code", response2.status_code)
response_dict2 = response2.json()
print(response_dict2.keys())


drug_interactions = response_dict2["results"][0]["drug_interactions"][0]
print(drug_interactions)



# #This will print out the dictionary's results
# print(response_dict2.get('results'))


# openfda.brand_name
# openfda.generic_name
# openfda.manufacturer_name
# openfda.substance_name

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)



# Basic API call
# https://api.fda.gov/drug/label.json/?search=drug_interactions:caffeine&limit=5