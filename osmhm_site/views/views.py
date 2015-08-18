from pyramid.response import Response
from pyramid.view import view_config

from ..models import (
    DBSession,
    History,
    Users,
    Objects,
    )


@view_config(route_name='home', renderer='osmhm:templates/home.mako')
def my_view(request):

    return dict(page_id="home")
