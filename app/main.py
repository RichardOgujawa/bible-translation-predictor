"""# IMPORTS"""
from flask import Flask
from dotenv import dotenv_values
import requests
import json
import pandas as pd

"""# SETUP"""
## Load in environment variables
config = dotenv_values(".env") 
API_KEY=config['API_TOKEN']

## Setup application
app = Flask(__name__)

"""# MODEL"""
HEADERS = {'api-key': API_KEY}

# ## Fetch data for bible translations
# def get_bible_versions(see_keys=False):
#     url="https://api.scripture.api.bible/v1/bibles"
#     # Get the response object from the fetch
#     response = requests.request("GET", url, headers=HEADERS)
#     # Convert the text to a json
#     data = json.loads(response.text)['data']
#     if see_keys:
#         print(data[0].keys())
#     df = pd.DataFrame(columns=['id', 'abbreviation', 'name', 'language'], data=data)
#     # Only return language name in language column, not entire dictionary
#     df['language'] = df['language'].apply(lambda x: x['name'])
#     # Return only english bibles
#     eng_df = df[df['language'] == 'English']
#     return eng_df

# ## Fetch data for chapters in the bible translation
# def get_books_in_bible(bibleId, see_keys=False):
#     url = f"https://api.scripture.api.bible/v1/bibles/{bibleId}/books"
#     # Get the response object from the fetch
#     response = requests.request("GET", url, headers=HEADERS)
#     # Convert the text to a json
#     data = json.loads(response.text)['data']
#     if see_keys:
#         print(data[0].keys())
#     df = pd.DataFrame(columns=['id', 'nameLong'], data=data)
#     return df
    
# bible_versions_df = get_bible_versions()
# print(bible_versions_df)

# BSB_id = bible_versions_df[bible_versions_df['name'] == 'Berean Standard Bible']['id'].values[0]
# # Get the books in the BSB
# bible_books_df = get_books_in_bible(BSB_id, see_keys=True)
# print(bible_books_df)
# ## Fetch data for verses in the bible translations chapter
# bible_verse_api_url="https://api.scripture.api.bible/v1/bibles/bibleId/chapters/chapterId/verses"
# print(response.text)



## Get data from bible api

# Homepage
@app.route('/')
def home():
    return '<h1>Bible Translation Predictor📖</h1>'

# # Predict translation
# @app.route('/input/<user-input>')
# def predict(input):
#     return model.predict(input)

# if __name__=='__main__':
#     app.run(debug=True)