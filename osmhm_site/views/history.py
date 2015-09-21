from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPUnauthorized
from pyramid.security import authenticated_userid

from pyramid.url import route_path
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized,
    HTTPBadRequest,
)

from sqlalchemy.exc import DBAPIError

from sqlalchemy import desc

from ..models import (
    DBSession,
    History,
    File_List,
    User,
)

@view_config(route_name='history', renderer='osmhm_site:templates/history.mako')
def watch(request):
	try:
		history = DBSession.query(History).order_by(desc(History.changeset)).all()
		filetime = DBSession.query(File_List).first()
	except DBAPIError:
		print 'Sorry'
	if not history:
		history = None
	return dict(page_id='history', history=history, update_time=filetime.timestamp)

@view_config(route_name='history_clear', permission='edit_user_or_object')
def watch_list(request):
	thedata = DBSession.query(History).delete()

	DBSession.flush()

	return HTTPFound(location=route_path('admin',request))
