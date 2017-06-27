from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.httpexceptions import HTTPFound

from .models import (
	DBSession,
	Base,
	)

from .security import (
    RootFactory,
    group_membership,
)

from pyramid.view import forbidden_view_config

@forbidden_view_config()
def forbidden(request):
    return HTTPFound(location=request.route_path('login'))

def main(global_config, **settings):
	engine = engine_from_config(settings, 'sqlalchemy.')
	DBSession.configure(bind=engine)
	Base.metadata.bind = engine

	authn_policy = AuthTktAuthenticationPolicy(
                         secret='super_secret',
                         callback=group_membership)
	authz_policy = ACLAuthorizationPolicy()

	config = Configurator(settings=settings,
                          root_factory=RootFactory,
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy)

	session_factory = UnencryptedCookieSessionFactoryConfig('itsasecret')
	config.set_session_factory(session_factory)

	config.include('pyramid_mako')
	config.add_static_view('static', 'static', cache_max_age=3600)

	config.add_route('home', '/')

	config.add_route('history', '/history')
	config.add_route('history_clear', '/history/clear')

	config.add_route('watch', '/watch')
	config.add_route('watch_whitelist', '/watch/whitelist')
	config.add_route('watch_whitelist_add', '/watch/whitelist/add')
	config.add_route('watch_whitelist_delete', '/watch/whitelist/delete/{id}')
	config.add_route('watch_clear', '/watch/clear')

	config.add_route('user_watch', '/user_watch')
	config.add_route('user_watch_event_delete', '/user_watch_event/delete/{id}')
	config.add_route('user_watch_list', '/user_watch/list')
	config.add_route('user_watch_add', '/user_watch/add')
        config.add_route('user_watch_edit', '/user_watch/edit/{id}')
	config.add_route('user_watch_delete', '/user_watch/delete/{id}')

	config.add_route('object_watch', '/object_watch')
	config.add_route('object_watch_event_delete', '/object_watch_event/delete/{id}')
	config.add_route('object_watch_clear', '/object_watch/clear')
	config.add_route('object_watch_list', '/object_watch/list')
	config.add_route('object_watch_add', '/object_watch/add')
        config.add_route('object_watch_edit', '/object_watch/edit/{id}')
	config.add_route('object_watch_delete', '/object_watch/delete/{id}')

	config.add_route('key_watch', '/key_watch')
	config.add_route('key_watch_event_delete', '/key_watch_event/delete/{username}/{key}/{value}')
	config.add_route('key_watch_clear', '/key_watch/clear')
	config.add_route('key_watch_list', '/key_watch/list')
	config.add_route('key_watch_add', '/key_watch/add')
        config.add_route('key_watch_edit', '/key_watch/edit/{id}')
	config.add_route('key_watch_delete', '/key_watch/delete/{id}')

	config.add_route('login', '/login')
	config.add_route('logout', '/logout')
	config.add_route('oauth_callback', '/oauth_callback')

	config.add_route('admin', '/admin')
	config.add_route('admin_user_list', '/admin/users')
	config.add_route('promote_member','/admin/{id}/promote_member')
	config.add_route('promote_admin','/admin/{id}/promote_admin')
	config.add_route('promote_owner','/admin/{id}/promote_owner')
	config.add_route('admin_clear_history', '/admin/clear_history',request_method="DELETE")

	config.scan()
	return config.make_wsgi_app()
