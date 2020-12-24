from parse import parse_csv_to_dict
import requests
import json

CLIENT_ID = 'REDACTED'
CLIENT_SECRET = 'REDACTED'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token),
    'Content-Type': 'application/json',
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

data = parse_csv_to_dict()

# print(data)

for row in data[:3]:
    track = row[0].replace(' ', '+')
    artist = row[1].replace(' ', '+')
    album = row[2].replace(' ', '=')

    # print('Track: ' + track + ' Artist: ' + artist + ' Album: ' + album)
    search_track = requests.get(BASE_URL + 'search?q=' + track + ' ' + artist + '&type=track&limit=1',
                     headers=headers
                     )
    search_track = search_track.json()
    #print(r)

    track_list = search_track['tracks']['items']
    print(track_list)

    for tracks in track_list:
        track_id = tracks['id']
        print(track_id)

    payload = {"ids": }
    #Add to spotify library
    add_track = requests.put(BASE_URL + 'me/tracks',
                             content-type=application/json,
                             scope=user-library-modify)




