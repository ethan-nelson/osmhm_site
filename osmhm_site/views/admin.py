from pyramid.response import Response
from pyramid.view import view_config
from pyramid.url import route_path
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized,
    HTTPBadRequest,
)

from ..models import (
    DBSession,
    User,
)

@view_config(route_name='admin', renderer='osmhm_site:templates/admin.mako',
             permission='edit_user_or_object')
def admin(request):
    
    return dict(page_id='admin')

@view_config(route_name='admin_user_list', renderer='osmhm_site:templates/admin_user_list.mako',
             permission='super_admin')
def admin_user_list(request):
	users = DBSession.query(User).all()
	users.sort(key=lambda user: user.username)

	return dict(page_id='users', users=users)

@view_config(route_name='promote_dwg', permission='super_admin')
def promote_dwg(request):
	userid = request.matchdict['id']
	promuser = DBSession.query(User).get(userid)

	promuser.role = User.role_dwg if not promuser.is_dwg else None
	DBSession.flush()

	return HTTPFound(location=route_path('admin_user_list',request))

@view_config(route_name='promote_admin', permission='super_admin')
def promote_admin(request):
	userid = request.matchdict['id']
	promuser = DBSession.query(User).get(userid)

	promuser.role = User.role_admin if not promuser.is_admin else None
	DBSession.flush()

	return HTTPFound(location=route_path('admin_user_list',request))

@view_config(route_name='promote_owner', permission='super_admin')
def promote_owner(request):
	userid = request.matchdict['id']
	promuser = DBSession.query(User).get(userid)

	promuser.role = User.role_owner if not promuser.is_owner else None
	DBSession.flush()

	return HTTPFound(location=route_path('admin_user_list',request))
