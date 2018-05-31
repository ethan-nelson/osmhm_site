from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPUnauthorized
from pyramid.security import authenticated_userid

from sqlalchemy.exc import DBAPIError

from sqlalchemy import desc,and_,distinct,func

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
                userid = authenticated_userid(request)
		full_history = DBSession.query(History_Keys).filter(Watched_Keys.authorid == userid).join(Watched_Keys, History_Keys.wid == Watched_Keys.id).order_by(desc(History_Keys.changeset)).all()
		history = DBSession.query(History_Keys).filter(Watched_Keys.authorid == userid).join(Watched_Keys, History_Keys.wid == Watched_Keys.id).distinct(History_Keys.username, History_Keys.key, History_Keys.value).all()

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
				changeset_strs[event.username][event.key][event.value] += ('<a href="https://www.openstreetmap.org/changeset/%s" target="_blank">%s</a> (%s), ' % (str(event.changeset), str(event.changeset), str(event.timestamp)))
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
	return dict(page_id='key_watch', history=history, update_time=filetime.timestamp)


@view_config(route_name='key_watch_event_delete', permission='edit_user_or_object')
def key_watch_event_delete(request):
    DBSession.query(History_Keys).filter_by(username=request.matchdict['username'], key=request.matchdict['key'], value=request.matchdict['value']).delete()
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
                userid = authenticated_userid(request)
		keys = DBSession.query(Watched_Keys).filter(Watched_Keys.authorid == userid).all()
	except DBAPIError:
		print 'Sorry'
	if not keys:
		keys = None
	return dict(page_id='key_watch_list', keys=keys)


@view_config(route_name='key_watch_add', renderer='osmhm_site:templates/key_watch_list_add.mako',
             permission='edit_user_or_object')
def key_watch_add(request):
    if request.method == 'POST':
        userid = authenticated_userid(request)
        if userid:
            user = DBSession.query(User).get(userid)
            keyToAdd = Watched_Keys(author=user.username,
                                  authorid=userid,
                                  key=request.POST.getone('addkey'),
                                  value=request.POST.getone('addvalue'),
                                  reason=request.POST.getone('addreason'),
                                  email=request.POST.getone('addnotify'))
    
            DBSession.add(keyToAdd)
            DBSession.flush()

            return HTTPFound(location=request.route_path('key_watch_list'))
        else:
            return HTTPUnauthorized()

    return dict(page_id='key_watch_add', data=None)


@view_config(route_name='key_watch_edit', renderer='osmhm_site:templates/key_watch_list_add.mako',
             permission='edit_user_or_object')
def key_watch_edit(request):
    userid = authenticated_userid(request)
    if userid:
        entry = DBSession.query(Watched_Keys).get(request.matchdict['id'])
        if int(userid) != entry.authorid:
            return HTTPUnauthorized()

        if request.method == 'POST':
            entry.key = request.POST.getone('addkey')
            entry.value = request.POST.getone('addvalue')
            entry.reason = request.POST.getone('addreason')
            entry.email = request.POST.getone('addnotify')

            DBSession.add(entry)
            DBSession.flush()

            return HTTPFound(location=request.route_path('key_watch_list'))

        else:
            return dict(page_id='key_watch_add', data=entry)

    else:
        return HTTPUnauthorized()


@view_config(route_name='key_watch_delete', permission='edit_user_or_object')
def key_watch_delete(request):
    userid = authenticated_userid(request)

    keyToDelete = DBSession.query(Watched_Keys).get(request.matchdict['id'])
    if int(keyToDelete.authorid) == int(userid):
        DBSession.query(History_Keys).filter_by(key=keyToDelete.key).delete()

        DBSession.delete(keyToDelete)
        DBSession.flush()

    return HTTPFound(location=request.route_path('key_watch_list'))

