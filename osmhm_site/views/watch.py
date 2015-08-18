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
    Users,
    User,
    Objects,
    Filetime,
    Whitelist,
)

@view_config(route_name='watch', renderer='osmhm_site:templates/watch.mako')
def watch(request):
	try:
		history = DBSession.query(History).order_by(desc(History.changeset)).all()
		filetime = DBSession.query(Filetime).first()
	except DBAPIError:
		print 'Sorry'
	if not history:
		history = None
	return dict(page_id='watch', history=history, update_time=filetime.timestamp)

@view_config(route_name='watch_clear', permission='edit_user_or_object')
def watch_list(request):
	thedata = DBSession.query(History).delete()

	DBSession.flush()

	return HTTPFound(location=route_path('admin',request))

@view_config(route_name='watch_whitelist', renderer='osmhm_site:templates/watch_whitelist.mako', permission='edit_user_or_object')
def watch_whitelist(request):
    try:
        users = DBSession.query(Whitelist).all()
    except DBAPIError:
        print 'Sorry'
    if not users:
        users = None
    return dict(page_id='watch_whitelist', users=users)

@view_config(route_name='watch_whitelist_add', renderer='osmhm_site:templates/admin_whitelist_add.mako', permission='edit_user_or_object')
def watch_whitelist_add(request):
    if request.method == 'POST':
        userid = authenticated_userid(request)
        if userid:
            user = DBSession.query(User).get(userid)
            userToAdd = Whitelist(author=user.username,
                                  username=request.POST.getone('addusername'),
                                  reason=request.POST.getone('addreason'))

            DBSession.add(userToAdd)
            DBSession.flush()
            return HTTPFound(location=request.route_path('watch_whitelist'))
        else:
            return HTTPUnauthorized()

    return dict(page_id='watch_whitelist_add')

@view_config(route_name='watch_whitelist_delete', permission='edit_user_or_object')
def watch_watchlist_delete(request):
    userToDelete = DBSession.query(Whitelist).get(request.matchdict['id'])
    DBSession.delete(userToDelete)
    DBSession.flush()

    return HTTPFound(location=request.route_path('watch_whitelist'))
