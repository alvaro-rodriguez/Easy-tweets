from bottle import default_app, get, post, template, request, static_file, response,redirect
import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
from urlparse import parse_qs
import json
import os
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "jWdjfLA3SbvWNPnE7G8LyoEAI"
CONSUMER_SECRET = "zOuclYiBmfKDztZaKtd77KL0hPf2DbvaQfbYDNNn83P6d3ldue"

def get_request_token():
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
    )
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["request_token"] = credentials.get('oauth_token')[0]
    TOKENS["request_token_secret"] = credentials.get('oauth_token_secret')[0]
    
def get_access_token(TOKENS):
  
  oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["request_token"],
                   resource_owner_secret=TOKENS["request_token_secret"],
                   verifier=TOKENS["verifier"],)
  
  
  r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
  credentials = parse_qs(r.content)
  TOKENS["access_token"] = credentials.get('oauth_token')[0]
  TOKENS["access_token_secret"] = credentials.get('oauth_token_secret')[0]

@get('/')
def index():
  return template('index.tpl')

@get('/twitter')
def twitter():
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    response.set_cookie("request_token", TOKENS["request_token"],secret='some-secret-key')
    response.set_cookie("request_token_secret", TOKENS["request_token_secret"],secret='some-secret-key')
    return template('oauth1.tpl', authorize_url=authorize_url)

@get('/callback')

def get_verifier():
  TOKENS["request_token"]=request.get_cookie("request_token", secret='some-secret-key')
  TOKENS["request_token_secret"]=request.get_cookie("request_token_secret", secret='some-secret-key')
  TOKENS["verifier"] = request.query.oauth_verifier
  get_access_token(TOKENS)
  response.set_cookie("access_token", TOKENS["access_token"],secret='some-secret-key')
  response.set_cookie("access_token_secret", TOKENS["access_token_secret"],secret='some-secret-key')
  redirect('/twittear')

 
@route('/hello')
def index():
    return '<strong>Hello World!</strong>'

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
