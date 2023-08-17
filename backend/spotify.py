import requests

CLIENT_ID = '7d16366b3ae34465a0561cd91120c3e6'
CLIENT_SECRET = 'c3e0c461a745496b8e270863a7efb90a'
REDIRECT_URI = 'http://localhost:3000/' 

# Gets the url for user to login
def get_authorization_url(client_id, redirect_uri):
    auth_url = 'https://accounts.spotify.com/authorize'
    scope = 'user-read-private user-read-email playlist-modify-public playlist-modify-private'  # Define the scopes your app needs
    params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope': scope,
    }
    response = requests.get(auth_url, params=params)
    authorization_url = response.url
    return authorization_url

# Gets the authorization code
def extract_authorization_code(callback_url):
    import urllib.parse
    parsed_url = urllib.parse.urlparse(callback_url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    authorization_code = query_params.get('code')
    return authorization_code

# Calls the function that extracts the authorization code
def handle_authorization_callback(callback_url):
        # Extract the authorization code from the callback URL
        authorization_code = extract_authorization_code(callback_url)
        return authorization_code

# Gets access token that will be used for the application
def get_access_token(authorization_code, client_id, client_secret, redirect_uri):
    token_url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get('access_token')
    return access_token

def authorize(client_id, client_secret, redirect_uri):
    auth_url = get_authorization_url(client_id, redirect_uri)
    print("Please visit the following URL to authorize the app:")
    print(auth_url)

def authorize_two(client_id, client_secret, redirect_uri):
    # Simulate the callback URL with the authorization code received from the user
    # Replace 'YOUR_CALLBACK_URL' with the actual URL the user was redirected to.
    callback_url = 'http://localhost:3000/?code=AQCaAK6GyFcnyn3eE70Wr-hUtPohzRqFRPvtBfr5EV3IYSv0xdDIMvFKx2CDkO4tV8FUDhqGL6qb9-IDe0eCgFhA0n0NHu9VJ3cSrqZTotPoER5YyaqGmC7N5Aa39SRtgtRU5AYHO5k8laKjcRNuAOwMMpC7pRsmcnkkz-4rVlPhA9cMljGJGSm46VKE9Nd30iDdQkwgnF8L8JSjEo4IGXj3qi24S7xquvy2XS-V7_dRceqex_LvHX2B-Xqv566e0W8nueoF_TXX0CMg4kHa'
    authorization_code = handle_authorization_callback(callback_url)
    print("Authorization code:", authorization_code)
    
    # Use the authorization code obtained earlier to get the access token
    access_token = get_access_token(authorization_code, client_id, client_secret, redirect_uri)
    print("Access token:", access_token)
    return access_token

authorize(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
# authorize_two(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)


# Use the authorization code obtained earlier to get the access token
# access_token = authorize(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
# print("Access token:", access_token)

def get_playlist_isrc(access_token, playlist_id):

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    playlist_base = 'https://api.spotify.com/v1/playlists/'
    additional = '/tracks?offset='

    offset = '0'
    r = requests.get(playlist_base + playlist_id + additional + offset, headers=headers)
    r = r.json()

    print(r)
    # Keep calling until all tracks are done
    num_tracks = r['total']
    num_accessed = 0

    isrc_list = []
    while num_accessed < num_tracks:

        r = requests.get(playlist_base + playlist_id + additional + offset, headers=headers)
        r = r.json()
        
        tracks = list(r['items'])

        for track in tracks:
            print(track['track']['name'])
            print(track['track']['artists'][0]['name'])
            print(track['track']['external_ids']['isrc'])
            isrc_list.append(track['track']['external_ids']['isrc'])
            print('\n')
            num_accessed += 1

        offset = str(num_accessed)
    return isrc_list

my_playlist_7 = '70YztKLiQMs5e6Ch7eB2YF'
my_inner_yash = '6B6A7gSEqWWTDVkQmZhGTH'
chill = '1yJs5UUWVKDIGTRqCp06Wa'
elite_playlist = '6hRRvWIvoEF8vKTyJmBj6K'
garbage_tester = '1XWbsDIPIy6yc4Wm7LrKrv'

# get_playlist_isrc(access_token, garbage_tester)
# isrc_list = get_playlist_isrc(access_token, my_inner_yash)
# print(isrc_list)


def add_songs_to_playlist(access_token, playlist_id, songs_list):
    playlist_base = 'https://api.spotify.com/v1/playlists/1XWbsDIPIy6yc4Wm7LrKrv/tracks'

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token),
        'Content-Type': 'application/json'  # Specify the content type as JSON
    }

    data = {
        "uris": ['spotify:track:23ezmwqqSKAqXYTiXQ60sf']
    }
    requests.post(playlist_base, headers=headers, json=data)
    

# add_songs_to_playlist(access_token, garbage_tester, [])