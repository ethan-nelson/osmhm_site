from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPUnauthorized
from pyramid.security import authenticated_userid

from sqlalchemy.exc import DBAPIError

from sqlalchemy import desc,and_

from ..models import (
    DBSession,
    Watched_Keys,
    History_Keys,
    File_List,
    User,
)

@view_config(route_name='key_watch', renderer='osmhm_site:templates/key_watch.mako',
             permission='watch_user_or_object')
def key_watch(request):
	try:
		history = DBSession.query(History_Keys).order_by(desc(History_Keys.changeset)).all()
		filetime = DBSession.query(File_List).first()
	except DBAPIError:
		print 'Sorry'
	if not history:
		history = None
	return dict(page_id='key_watch', history=history, update_time=filetime.timestamp)


@view_config(route_name='key_watch_event_delete', permission='edit_user_or_object')
def key_watch_event_delete(request):
    DBSession.query(History_Keys).filter_by(id=request.matchdict['id']).delete()
    DBSession.flush()

    return HTTPFound(location=request.route_path('key_watch'))


@view_config(route_name='key_watch_clear', permission='edit_user_or_object')
def key_watch_clear(request):
    DBSession.query(History_Keys).delete()
    DBSession.flush()

    return HTTPFound(location=request.route_path('key_watch'))

@view_config(route_name='key_watch_list', renderer='osmhm_site:templates/key_watch_list.mako',
             permission='watch_user_or_object')
def key_watch_list(request):
	try:
		keys = DBSession.query(Watched_Keys).all()
	except DBAPIError:
		print 'Sorry'
	if not keys:
		keys = None
	return dict(page_id='key_watch_list', keys=keys)


@view_config(route_name='key_watch_add', renderer='osmhm_site:templates/admin_key_list_add.mako',
             permission='edit_user_or_object')
def key_watch_add(request):
    if request.method == 'POST':
        userid = authenticated_userid(request)
        if userid:
            user = DBSession.query(User).get(userid)
            keyToAdd = Watched_Keys(author=user.username,
                                  key=request.POST.getone('addkey'),
                                  value=request.POST.getone('addvalue'),
                                  reason=request.POST.getone('addreason'),
                                  email=request.POST.getone('addnotify'))
    
            DBSession.add(keyToAdd)
            DBSession.flush()

            return HTTPFound(location=request.route_path('key_watch_list'))
        else:
            return HTTPUnauthorized()

    return dict(page_id='key_watch_add')


@view_config(route_name='key_watch_delete', permission='edit_user_or_object')
def key_watch_delete(request):
    keyToDelete = DBSession.query(Watched_Keys).get(request.matchdict['id'])
    eventsToDelete = DBSession.query(History_Keys).filter_by(key=keyToDelete.key).delete()
    DBSession.delete(keyToDelete)
    DBSession.flush()

    return HTTPFound(location=request.route_path('key_watch_list'))

