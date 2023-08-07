from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__) #????

CORS(app)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/token')
def get_access_token():

    CLIENT_ID = '7d16366b3ae34465a0561cd91120c3e6'
    CLIENT_SECRET = '418d03b59b3e45ebac2837aedce75580'

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    auth_response_data = auth_response.json()
    return auth_response_data['access_token']





if __name__ == '__main__':
    app.run(debug=True, port=5500)