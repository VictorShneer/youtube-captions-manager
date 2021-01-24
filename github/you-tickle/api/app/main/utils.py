import requests

def request_new_token():
    json={'email':'susan@example.com', 'p':'91Afr1caTickle1!'}
    r = requests.post('https://your-tickle-db.herokuapp.com/ligon', json=json)
    return r.json()['token']

def write_captions(captions, token):
    r = requests.post(f'https://your-tickle-db.herokuapp.com/write_caption/{token}', json=captions)
    return r