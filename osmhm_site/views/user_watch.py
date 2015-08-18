from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPUnauthorized
from pyramid.security import authenticated_userid

from sqlalchemy.exc import DBAPIError

from sqlalchemy import desc

from ..models import (
    DBSession,
    History,
    Users,
    UserHistory,
    Objects,
    ObjectHistory,
    Filetime,
    User,
)

@view_config(route_name='user_watch', renderer='osmhm:templates/user_watch.mako',
             permission='watch_user_or_object')
def user_watch(request):
	try:
		history = DBSession.query(UserHistory).order_by(desc(UserHistory.changeset)).all()
		filetime = DBSession.query(Filetime).first()
	except DBAPIError:
		print 'Sorry'
	if not history:
		history = None
	return dict(page_id='user_watch', history=history, update_time=filetime.timestamp)

@view_config(route_name='user_watch_list', renderer='osmhm:templates/user_watch_list.mako',
             permission='watch_user_or_object')
def user_watch_list(request):
	try:
		users = DBSession.query(Users).all()
	except DBAPIError:
		print 'Sorry'
	if not users:
		users = None
	return dict(page_id='user_watch_list', users=users)

@view_config(route_name='user_watch_add', renderer='osmhm:templates/admin_user_list_add.mako',
             permission='edit_user_or_object')
def user_watch_add(request):

    if request.method == 'POST':
        userid = authenticated_userid(request)
        if userid:
            user = DBSession.query(User).get(userid)
            userToAdd = Users(author=user.username,
                              username=request.POST.getone('addusername'),
                              reason=request.POST.getone('addreason'),
                              email=request.POST.getone('addnotify'))
    
            DBSession.add(userToAdd)
            DBSession.flush()

            return HTTPFound(location=request.route_path('user_watch_list'))
        else:
            return HTTPUnauthorized()

    return dict(page_id='user_watch_add')

@view_config(route_name='user_watch_delete', permission='edit_user_or_object')
def user_watch_delete(request):
    userToDelete = DBSession.query(Users).get(request.matchdict['id'])
    eventsToDelete = DBSession.query(UserHistory).filter_by(username=userToDelete.username).delete()
    DBSession.delete(userToDelete)
    DBSession.flush()

    return HTTPFound(location=request.route_path('user_watch_list'))

