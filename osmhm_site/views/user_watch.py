from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPUnauthorized
from pyramid.security import authenticated_userid

from sqlalchemy.exc import DBAPIError

from sqlalchemy import desc

from ..models import (
    DBSession,
    Watched_Users,
    History_Users,
    File_List,
    User,
)

@view_config(route_name='user_watch', renderer='osmhm_site:templates/user_watch.mako',
             permission='watch_user_or_object')
def user_watch(request):
	try:
                userid = authenticated_userid(request)
		history = DBSession.query(History_Users, Watched_Users).filter(Watched_Users.authorid == userid).join(Watched_Users, History_Users.wid == Watched_Users.id).order_by(desc(History_Users.changeset)).all()
		filetime = DBSession.query(File_List).first()
	except DBAPIError:
		print 'Sorry'
#        history = None
#	if not history:
#		history = None
	return dict(page_id='user_watch', history=history, update_time=filetime.timestamp)

@view_config(route_name='user_watch_event_delete', permission='edit_user_or_object')
def user_watch_event_delete(request):
    DBSession.query(History_Users).filter_by(id=request.matchdict['id']).delete()
    DBSession.flush()

    return HTTPFound(location=request.route_path('user_watch'))

@view_config(route_name='user_watch_list', renderer='osmhm_site:templates/user_watch_list.mako',
             permission='watch_user_or_object')
def user_watch_list(request):
	try:
                userid = authenticated_userid(request)
		users = DBSession.query(Watched_Users).filter(Watched_Users.authorid == userid).all()
	except:
		print 'Sorry'
#	except DBAPIError:
#		print 'Sorry'
#        users = None
#	if not users:
#		users = None

	return dict(page_id='user_watch_list', users=users)

@view_config(route_name='user_watch_add', renderer='osmhm_site:templates/user_watch_list_add.mako',
             permission='edit_user_or_object')
def user_watch_add(request):

    if request.method == 'POST':
        userid = authenticated_userid(request)
        if userid:
            user = DBSession.query(User).get(userid)
            userToAdd = Watched_Users(author=user.username,
                              authorid=userid,
                              username=request.POST.getone('addusername'),
                              reason=request.POST.getone('addreason'),
                              email=request.POST.getone('addnotify'))
    
            DBSession.add(userToAdd)
            DBSession.flush()

            return HTTPFound(location=request.route_path('user_watch_list'))
        else:
            return HTTPUnauthorized()

    return dict(page_id='user_watch_add', data=None)

@view_config(route_name='user_watch_edit', renderer='osmhm_site:templates/user_watch_list_add.mako',
             permission='edit_user_or_object')
def user_watch_edit(request):
    userid = authenticated_userid(request)
    if userid:
        entry = DBSession.query(Watched_Users).get(request.matchdict['id'])
        if int(userid) != entry.authorid:
            return HTTPUnauthorized()

        if request.method == 'POST':
            entry.username = request.POST.getone('addusername')
            entry.reason = request.POST.getone('addreason')
            entry.email = request.POST.getone('addnotify')

            DBSession.add(entry)
            DBSession.flush()

            return HTTPFound(location=request.route_path('user_watch_list'))

        else:
            return dict(page_id='user_watch_add', data=entry)

    else:
        return HTTPUnauthorized()

@view_config(route_name='user_watch_delete', permission='edit_user_or_object')
def user_watch_delete(request):
    userid = authenticated_userid(request)

    userToDelete = DBSession.query(Watched_Users).get(request.matchdict['id'])
    if int(userToDelete.authorid) == int(userid):
        DBSession.query(History_Users).filter_by(wid=userToDelete.id).delete()

        DBSession.delete(userToDelete)
        DBSession.flush()

    return HTTPFound(location=request.route_path('user_watch_list'))

