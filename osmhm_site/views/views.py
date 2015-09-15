from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='osmhm_site:templates/home.mako')
def my_view(request):

    return dict(page_id="home")
