# coding=utf-8
import os
import urllib
import webbrowser

import requests


CLIENT_ID = '953873850388-atdql57lc2m0v4ngkheb2ppaap7846bo.apps.googleusercontent.com'
CLIENT_SECRET = 'hnm-HA8_ZMYRVQDTdyg8a_kk'
SCOPE = 'https://spreadsheets.google.com/feeds'
REDIRECT_URL = 'https://storage.googleapis.com/arakawatomonori-wakari-web/auth_complete.html'
SAVE_PATH = './.oauth_token'


def run():
    query = {
        'scope': SCOPE,
        'state': 'something',
        'redirect_uri': REDIRECT_URL,
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'approval_prompt': 'force',
        'access_type': 'offline',
    }
    params = urllib.urlencode(query)
    url = 'https://accounts.google.com/o/oauth2/auth?{0}'.format(params)
    print('Opening authorization URL, please follow the instructions then copy/paste the "code" param here.')
    print(url)
    webbrowser.open_new_tab(url)

    code = raw_input('Code: ')

    payload = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URL,
        'grant_type': 'authorization_code',
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url = 'https://accounts.google.com/o/oauth2/token'
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()

    save(response.content)

    tokens = response.json()
    print('Access Token: {0}'.format(tokens['access_token']))
    print('Refresh Token: {0}'.format(tokens['refresh_token']))


def save(token_json):
    open(SAVE_PATH, 'w').write(token_json)
    os.chmod(SAVE_PATH, 0400)


if __name__ == '__main__':
    run()
