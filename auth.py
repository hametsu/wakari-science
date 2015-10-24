# coding=utf-8
import os
import webbrowser

from oauth2client import client


CLIENT_SECRET = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'client_secret.json')
SAVE_PATH = './.oauth_credentials'


def run():
    flow = client.flow_from_clientsecrets(
        CLIENT_SECRET,
        scope='https://spreadsheets.google.com/feeds',
        redirect_uri='https://storage.googleapis.com/arakawatomonori-wakari-web/auth_complete.html'
    )
    auth_uri = flow.step1_get_authorize_url()
    print('Opening authorization URL, please follow the instructions then copy/paste the "code" param here.')
    print(auth_uri)
    webbrowser.open_new_tab(auth_uri)

    auth_code = raw_input('Code: ')

    credentials = flow.step2_exchange(auth_code)
    save(credentials.to_json())
    print('Tokens Saved {0}'.format(SAVE_PATH))


def save(token_json):
    open(SAVE_PATH, 'w').write(token_json)
    os.chmod(SAVE_PATH, 0600)


if __name__ == '__main__':
    run()
