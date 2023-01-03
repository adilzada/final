import requests
# import praw

ENDPOINT = "https://www.reddit.com/"

def test_can_login():
    client_auth = requests.auth.HTTPBasicAuth('*******************', '*******************')
    post_data = {"grant_type": "password", "username": "****************", "password": "******************"}
    headers = {"User-Agent": "ChangeMeClient/0.1 by username"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = response.json()['access_token']
    print(TOKEN,"-------------------------")
    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    assert response.status_code == 200
    return headers

headers = test_can_login()

def test_can_call_friends():
    response1 = requests.get('https://oauth.reddit.com/api/v1/me/friends', headers=headers)
    assert response1.status_code == 200

def test_can_call_karma():
    response = requests.get('https://oauth.reddit.com/api/v1/me/karma', headers=headers)
    assert response.status_code == 200

def test_can_call_prefs():
    response = requests.get('https://oauth.reddit.com/api/v1/me/prefs', headers=headers)
    assert response.status_code == 200

def test_can_call_trophies():
    response = requests.get('https://oauth.reddit.com/api/v1/me/trophies', headers=headers)
    assert response.status_code == 200

def test_can_call_prefs_blocked():
    response = requests.get('https://oauth.reddit.com/prefs/blocked', headers=headers)
    assert response.status_code == 200

def test_can_call_prefs_friends():
    response = requests.get('https://oauth.reddit.com/prefs/friends', headers=headers)
    assert response.status_code == 200

def test_can_call_prefs_messaging():
    response = requests.get('https://oauth.reddit.com/prefs/messaging', headers=headers)
    assert response.status_code == 200

def test_can_call_prefs_trusted():
    response = requests.get('https://oauth.reddit.com/prefs/trusted', headers=headers)
    assert response.status_code == 200

def test_can_call_collections_collection():
    response = requests.get('https://oauth.reddit.com/api/v1/collections/collection', headers=headers)
    assert response.status_code == 200

def test_can_create_collection():
    post_data = {
        "description":"test",
        "display_layout": "TIMELINE",
        "sr_fullname": "t5_7okbdt",
        "title": "hello. it is test"}
    response = requests.post('https://oauth.reddit.com/api/v1/collections/create_collection', headers=headers, json=post_data)
    assert response.status_code == 200

def test_can_del():
    post_data = {
        "id":"t5_7okbdt"}
    response = requests.post('https://oauth.reddit.com/api/del', headers=headers, json=post_data)
    assert response.status_code == 200
