from pyramid.view import view_config
from xml.etree import ElementTree
from pyramid.httpexceptions import HTTPFound, HTTPBadGateway, HTTPBadRequest

from ..models import (
    DBSession,
    User,
)

from pyramid.security import (
    remember,
    forget,
)

import urlparse
import oauth2 as oauth

CONSUMER_KEY = 'IMjqoNHVuMaGOkIggHhasrqg08GcXULWtMjs742i'
CONSUMER_SECRET = '11tXVQCp50NpG3IBVo3R4fYIpjgbq24tL2FUuDXX'

BASE_URL = 'http://www.openstreetmap.org/oauth'
REQUEST_TOKEN_URL = '%s/request_token' % BASE_URL
ACCESS_TOKEN_URL = '%s/access_token' % BASE_URL
AUTHORIZE_URL = '%s/authorize' % BASE_URL

USER_DETAILS_URL = 'http://api.openstreetmap.org/api/0.6/user/details'

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)


@view_config(route_name='login')
def login(request):
    client = oauth.Client(consumer)
    oauth_callback_url = request.route_url('oauth_callback')
    url = "%s?oauth_callback=%s" % (REQUEST_TOKEN_URL, oauth_callback_url)
    resp, content = client.request(url, "GET")
    if resp['status'] != '200':
        return HTTPBadGateway('The OSM authentication server didn\'t\
                respond correctly')
    request_token = dict(urlparse.parse_qsl(content))
    session = request.session
    session['request_token'] = request_token
    session['came_from'] = request.params.get('came_from')
    redirect_url = "%s?oauth_token=%s" % \
                   (AUTHORIZE_URL, request_token['oauth_token'])
    return HTTPFound(location=redirect_url)


@view_config(route_name='oauth_callback')
def oauth_callback(request):
    session = request.session
    request_token = session.get('request_token')
    if request.params.get('oauth_token') != request_token['oauth_token']:
        return HTTPBadRequest('Tokens don\'t match')
    token = oauth.Token(request_token['oauth_token'],
                        request_token['oauth_token_secret'])
    verifier = request.params.get('oauth_verifier')
    token.set_verifier(verifier)
    client = oauth.Client(consumer, token)
    resp, content = client.request(ACCESS_TOKEN_URL, "POST")
    access_token = dict(urlparse.parse_qsl(content))
    token = access_token['oauth_token']
    token_secret = access_token['oauth_token_secret']
    token = oauth.Token(token, token_secret)
    client = oauth.Client(consumer, token)
    resp, content = client.request(USER_DETAILS_URL, "GET")
    user_elt = ElementTree.XML(content).find('user')

    if 'id' in user_elt.attrib:
        userid = user_elt.attrib['id']
        username = user_elt.attrib['display_name']

        user = DBSession.query(User).get(userid)
        if user is None:
            user = User(userid, username)
            DBSession.add(user)
            DBSession.flush()

        if DBSession.query(User).filter(User.role == User.role_owner) \
                    .count() == 0:
            user = DBSession.query(User).get(userid)
            user.role = User.role_owner

        headers = remember(request, userid, max_age=20 * 7 * 24 * 60 * 60)

    location = session.get('came_from') or request.route_path('home')
    return HTTPFound(location=location, headers=headers)


@view_config(route_name='logout')
def logout(request):  # pragma: no cover
    headers = forget(request)
    return HTTPFound(location=request.route_path('home'), headers=headers)
