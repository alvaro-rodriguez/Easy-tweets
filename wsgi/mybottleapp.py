# -*- encoding: utf-8 -*-
from bottle import default_app, get, post, template, request, static_file, response,redirect, route
import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
#from beaker.middleware import SessionMiddleware
from urlparse import parse_qs
import json
import os
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"


CONSUMER_KEY = "RV5QS2itE2SIeKhhiFU7XPChm"
CONSUMER_SECRET = "uUIGAC7OkEw14laGP0Wv10lBEiVmo1fdFMKzFJDBBc5JCyeEXB"

TOKENS = {}

###oauth1



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

username = None
@get('/')
@get('/<name>')
def twitter(name='nombre'):
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    response.set_cookie("request_token", TOKENS["request_token"],secret='some-secret-key')
    response.set_cookie("request_token_secret", TOKENS["request_token_secret"],secret='some-secret-key')
    return template('principal.tpl', authorize_url=authorize_url)
"""
@post('/')
def logeo():
  username = request.forms.get("nombre")
  print username
  print CONSUMER_KEY
  print CONSUMER_SECRET
  print TOKENS["access_token"]
  print TOKENS["access_token_secret"]
""" 
  
@get('/callback')
def get_verifier():
  TOKENS["request_token"]=request.get_cookie("request_token", secret='some-secret-key')
  TOKENS["request_token_secret"]=request.get_cookie("request_token_secret", secret='some-secret-key')
  TOKENS["verifier"] = request.query.oauth_verifier
  get_access_token(TOKENS)
  response.set_cookie("access_token", TOKENS["access_token"],secret='some-secret-key')
  response.set_cookie("access_token_secret", TOKENS["access_token_secret"],secret='some-secret-key')
  redirect('/menu')

@get('/menu')
def menu():
    return template('menu.tpl')
#-----------------------------------------------------------------------------------------
#publicar un tweet
@get('/twittear')
def twittear():
    if request.get_cookie("access_token", secret='some-secret-key'):
      TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
      TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
      return template('twittear.tpl')  
    else:
      redirect('/menu')


@post('/twittear')
def tweet_submit():
  texto = request.forms.get("twittear")
  TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
  TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
  print CONSUMER_KEY
  print CONSUMER_SECRET
  print TOKENS["access_token"]
  print TOKENS["access_token_secret"]
  oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
  url = 'https://api.twitter.com/1.1/statuses/update.json'
  r = requests.post(url=url,
                      data={"status":texto},
                      auth=oauth)
  if r.status_code == 200:
     redirect('/menu')
#    return "<p>Tweet properly sent</p>"
  else:
    return "<p>Unable to send tweet</p>"+r.content
#-----------------------------------------------------------------------------------------
#mensajes directos
@get('/mensaje')
@get('/mensaje/<name>')
def mensaje(name='nombre'):
    if request.get_cookie("access_token", secret='some-secret-key'):
      TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
      TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
      TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
      TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
      print CONSUMER_KEY
      print CONSUMER_SECRET
      print TOKENS["access_token"]
      print TOKENS["access_token_secret"]
      oauth = OAuth1(CONSUMER_KEY,
		    client_secret=CONSUMER_SECRET,
		    resource_owner_key=TOKENS["access_token"],
		    resource_owner_secret=TOKENS["access_token_secret"])
      #url='https://api.twitter.com/1.1/followers/list.json'
      url="https://api.twitter.com/1.1/followers/list.json?cursor=-1&screen_name=gatoapacheboina&skip_status=true&include_user_entities=false"
      r = requests.get(url=url,
		      #data={'cursor':'-1','screen_name':'gatoapacheboina','skip_status':'true','include_user_entities':'false'},
		      auth=oauth)
      doc=r.json()
      return template('mensaje.tpl',doc=doc,name=name)

@post('/mensaje')
def mensaje_submit():
    destino=request.forms.get('destino')
    texto = request.forms.get('mensaje')
    TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
    TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
    print CONSUMER_KEY
    print CONSUMER_SECRET
    print TOKENS["access_token"]
    print TOKENS["access_token_secret"]
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
    url = 'https://api.twitter.com/1.1/direct_messages/new.json'
    r = requests.post(url=url,
                      data={"text":texto,"screen_name":destino},
                      auth=oauth)
    if r.status_code == 200:
        return redirect('/menu')
    else:
        return "<p>Unable to send tweet</p>"+r.content
#-----------------------------------------------------------------------------------------
#historial de mensajes

@get('/mensajes')
def mensajes():
    TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
    TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
    print CONSUMER_KEY
    print CONSUMER_SECRET
    print TOKENS["access_token"]
    print TOKENS["access_token_secret"]
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
    url='https://api.twitter.com/1.1/direct_messages.json?count=90'
    r = requests.get(url=url,
                      #data={"screen_name":'gatoapacheboina','count':'2'},
                      auth=oauth)
    if r.status_code==200:
      doc=r.json()
      return template('mensajes.tpl',doc=doc) 
#    return doc
    #return url
"""if r.status_code == 200:
        doc=r.json()
        return doc
    else:
	doc=r.json()
        return doc

"""
#-----------------------------------------------------------------------------------------
#timeline del usuario
@get('/timeline')
def timeline():
    TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
    TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
    print CONSUMER_KEY
    print CONSUMER_SECRET
    print TOKENS["access_token"]
    print TOKENS["access_token_secret"]
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
    url='https://api.twitter.com/1.1/statuses/user_timeline.json'
    r = requests.get(url=url,
                      data={"screen_name":'gatoapacheboina','count':'2'},
                      auth=oauth)
    if r.status_code == 200:
        doc=r.json()
        return doc
    else:
	doc=r.json()
        return doc
#---------------------------------------------------------------------------------
#Estadisticas

@get('/estadisticas')
def estadisticas():
   return template('estadisticas.tpl') 
#----------------------------------------------
#Seguidores
@get('/seguidores')
def seguidores():
  
@post('/seguidores')
def seguidores_submit():
    TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
    TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
    print CONSUMER_KEY
    print CONSUMER_SECRET
    print TOKENS["access_token"]
    print TOKENS["access_token_secret"]
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
    #url='https://api.twitter.com/1.1/followers/list.json'
    screen_name= "gatoapacheboina" 
    url="https://api.twitter.com/1.1/followers/list.json?cursor=-1&"+screen_name+"&skip_status=true&include_user_entities=false"
    r = requests.get(url=url,
		     #data={'cursor':'-1','screen_name':'gatoapacheboina','skip_status':'true','include_user_entities':'false'},
		     auth=oauth)
    if r.status_code == 200:
        doc=r.json()
        #return doc
        return  template('seguidores.tpl',doc=doc)
    else:
        doc=r.json()
        return doc

#------------------------------------------------
#menciones

@get('/menciones')
def menciones():
    TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
    TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
    print CONSUMER_KEY
    print CONSUMER_SECRET
    print TOKENS["access_token"]
    print TOKENS["access_token_secret"]
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
    url='https://api.twitter.com/1.1/statuses/mentions_timeline.json?count=9'
    
    r = requests.get(url=url,
                      auth=oauth)
    if r.status_code == 200:
        doc=r.json()
        return template('menciones.tpl',doc=doc)
    else:
        doc=r.json()
        return doc
"""
@post('/menciones')
def tweet_submit():
    numero=request.forms.get('numero')
    TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
    TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
    print CONSUMER_KEY
    print CONSUMER_SECRET
    print TOKENS["access_token"]
    print TOKENS["access_token_secret"]
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
    url='https://api.twitter.com/1.1/statuses/user_timeline.json'
    r = requests.post(url=url,
                      data={"count":numero},
                      auth=oauth)
    if r.status_code != 200:
        doc=r.json()
        return template('menciones.tpl',doc=doc)
    else:
        doc=r.json()
        return doc
"""
#---------------------------------------------------
#Retweets

@get('/retweets')
def seguidores():
    TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
    TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
    print CONSUMER_KEY
    print CONSUMER_SECRET
    print TOKENS["access_token"]
    print TOKENS["access_token_secret"]
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
    
    url='https://api.twitter.com/1.1/statuses/retweets_of_me.json?count=500&amp;since_id=259320959964680190&amp;max_id=259320959964680500'
    r = requests.get(url=url, auth=oauth)
    if r.status_code == 200:
        doc=r.json()
        return doc
        #return template('seguidores.tpl',doc=doc)
    else:
        doc=r.json()
        return doc

"""
@post('/retweets')
def tweet_submit():
    numero=request.forms.get('numero')
    TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
    TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
    print CONSUMER_KEY
    print CONSUMER_SECRET
    print TOKENS["access_token"]
    print TOKENS["access_token_secret"]
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
    url='https://api.twitter.com/1.1/statuses/user_timeline.json'
    r = requests.post(url=url,
                      data={"count":texto},
                      auth=oauth)
    if r.status_code == 200:
        doc=r.json()
        return "<p>Tweet properly sent</p>"
    else:
        doc=r.json()
        return "<p>Unable to send tweet</p>"+r.content
"""
#---------------------------------------------------------------------------------
#Deconectar
@get('/twitter_logout')
def twitter_logout():
  response.set_cookie("access_token", '',max_age=0)
  response.set_cookie("access_token_secret", '',max_age=0)
  redirect('/')



# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 
application=default_app()
#application=app