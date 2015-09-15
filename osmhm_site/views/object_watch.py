from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPUnauthorized
from pyramid.security import authenticated_userid

from sqlalchemy.exc import DBAPIError

from sqlalchemy import desc

from ..models import (
    DBSession,
    Watched_Objects,
    History_Objects,
    File_List,
    User,
)

@view_config(route_name='object_watch', renderer='osmhm_site:templates/object_watch.mako',
             permission='watch_user_or_object')
def object_watch(request):
	try:
		history = DBSession.query(History_Objects).order_by(desc(History_Objects.changeset)).all()
		filetime = DBSession.query(File_List).first()
	except DBAPIError:
		print 'Sorry'
	if not history:
		history = None
	return dict(page_id='object_watch', history=history, update_time=filetime.timestamp)


@view_config(route_name='object_watch_list', renderer='osmhm_site:templates/object_watch_list.mako',
             permission='watch_user_or_object')
def object_watch_list(request):
	try:
		objects = DBSession.query(Watched_Objects).all()
	except DBAPIError:
		print 'Sorry'
	if not objects:
		objects = None
	return dict(page_id='object_watch_list', objects=objects)


@view_config(route_name='object_watch_add', renderer='osmhm_site:templates/admin_object_list_add.mako',
             permission='edit_user_or_object')
def object_watch_add(request):
    if request.method == 'POST':
        userid = authenticated_userid(request)
        if userid:
            user = DBSession.query(User).get(userid)
            objectToAdd = Watched_Objects(author=user.username,
                                  element=request.POST.getone('addobjectname'),
                                  reason=request.POST.getone('addreason'),
                                  email=request.POST.getone('addnotify'))
    
            DBSession.add(objectToAdd)
            DBSession.flush()

            return HTTPFound(location=request.route_path('object_watch_list'))
        else:
            return HTTPUnauthorized()

    return dict(page_id='object_watch_add')


@view_config(route_name='object_watch_delete', permission='edit_user_or_object')
def object_watch_delete(request):
    objectToDelete = DBSession.query(Watched_Objects).get(request.matchdict['id'])
    eventsToDelete = DBSession.query(History_Objects).filter_by(element=objectToDelete.element).delete()
    DBSession.delete(objectToDelete)
    DBSession.flush()

    return HTTPFound(location=request.route_path('object_watch_list'))

