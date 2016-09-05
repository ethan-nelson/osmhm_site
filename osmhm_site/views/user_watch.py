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
    Watched_Users_Objects,
    History_Users_Objects,
    File_List,
    User,
    User_Tags,
)

@view_config(route_name='user_watch', renderer='osmhm_site:templates/user_watch.mako',
             permission='watch_user_or_object')
def user_watch(request):
	try:
		history = DBSession.query(History_Users).order_by(desc(History_Users.changeset)).all()
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
		users = DBSession.query(Watched_Users).all()
	except:
		print 'Sorry'
#	except DBAPIError:
#		print 'Sorry'
#        users = None
#	if not users:
#		users = None

	return dict(page_id='user_watch_list', users=users)

@view_config(route_name='user_object_watch', renderer='osmhm_site:templates/user_object_watch.mako',
             permission='watch_user_or_object')
def user_object_watch(request):
	try:
		full_history = DBSession.query(History_Users_Objects).order_by(desc(History_Users_Objects.changeset)).all()
		history = DBSession.query(History_Users_Objects).distinct(History_Users_Objects.username, History_Users_Objects.key, History_Users_Objects.value).all()

		changesets = {}
		changeset_strs = {}
		objects = {}
		for event in full_history:
			if event.username not in changeset_strs:
				changesets[event.username] = {}
				changeset_strs[event.username] = {}
				objects[event.username] = {}
			if event.key not in changeset_strs[event.username]:
				changesets[event.username][event.key] = {}
				changeset_strs[event.username][event.key] = {}
				objects[event.username][event.key] = {}
			if event.value not in changeset_strs[event.username][event.key]:
				changesets[event.username][event.key][event.value] = []
				changeset_strs[event.username][event.key][event.value] = ''
				objects[event.username][event.key][event.value] = 0
			if event.changeset not in changesets[event.username][event.key][event.value]:
				changesets[event.username][event.key][event.value].append(event.changeset)
				changeset_strs[event.username][event.key][event.value] += ('<a href="http://www.openstreetmap.org/changeset/%s" target="_blank">%s</a> (%s), ' % (str(event.changeset), str(event.changeset), str(event.timestamp)))
			objects[event.username][event.key][event.value] += 1

		for event in history:
			event.changeset_count = len(changesets[event.username][event.key][event.value])
			event.object_count = objects[event.username][event.key][event.value]
			event.changesets = changeset_strs[event.username][event.key][event.value]

		filetime = DBSession.query(File_List).first()
	except DBAPIError:
		print 'Sorry'
	if not history:
		history = None
	return dict(page_id='user_object_watch', history=history, update_time=filetime.timestamp)


@view_config(route_name='user_object_watch_event_delete', permission='edit_user_or_object')
def key_watch_event_delete(request):
    DBSession.query(History_Users_Objects).filter_by(username=request.matchdict['username'], key=request.matchdict['key'], value=request.matchdict['value']).delete()
    DBSession.flush()

    return HTTPFound(location=request.route_path('user_object_watch'))


@view_config(route_name='user_object_watch_clear', permission='edit_user_or_object')
def key_watch_clear(request):
    DBSession.query(History_Users_Objects).delete()
    DBSession.flush()

    return HTTPFound(location=request.route_path('user_object_watch'))


@view_config(route_name='user_watch_add', renderer='osmhm_site:templates/admin_user_list_add.mako',
             permission='edit_user_or_object')
def user_watch_add(request):

    if request.method == 'POST':
        userid = authenticated_userid(request)
        if userid:
            user = DBSession.query(User).get(userid)
            userToAdd = Watched_Users(author=user.username,
                              username=request.POST.getone('addusername'),
                              reason=request.POST.getone('addreason'),
                              email=request.POST.getone('addnotify'))
    
            DBSession.add(userToAdd)
            count = 0
            for t in request.POST.keys():
                if t[0:4] == 'tag_':
                    tag = DBSession.query(User_Tags).get(t[4:])
                    userToAdd.tags.append(tag)
                    if count == 0:
                        suserToAdd = Watched_Users_Objects(author=user.username,
                                           username=request.POST.getone('addusername'),
                                           reason=request.POST.getone('addreason'),
                                           email=request.POST.getone('addnotify'))
                        DBSession.add(suserToAdd)
                    suserToAdd.tags.append(tag)
            if count != 0:
                DBSession.delete(userToAdd)

            DBSession.flush()

            return HTTPFound(location=request.route_path('user_watch_list'))
        else:
            return HTTPUnauthorized()

    tags = DBSession.query(User_Tags).all()

    return dict(page_id='user_watch_add', tags=tags)

@view_config(route_name='user_watch_delete', permission='edit_user_or_object')
def user_watch_delete(request):
    userToDelete = DBSession.query(Watched_Users).get(request.matchdict['id'])
    eventsToDelete = DBSession.query(History_Users).filter_by(username=userToDelete.username).delete()
    DBSession.delete(userToDelete)
    DBSession.flush()

    return HTTPFound(location=request.route_path('user_watch_list'))
