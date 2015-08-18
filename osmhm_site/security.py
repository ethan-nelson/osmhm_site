from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from zope.sqlalchemy import ZopeTransactionExtension

from .models import (
    User,
)

from pyramid.security import (
    Allow,
    Everyone,
    Deny,
)

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

class RootFactory(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, 'group:dwg', 'watch_user_or_object'),
        (Allow, 'group:dwg', 'edit_user_or_object'),
        (Allow, 'group:admin', 'watch_user_or_object'),
        (Allow, 'group:admin', 'edit_user_or_object'),
        (Allow, 'group:admin', 'super_admin'),
    ]
    def __init__(self, request):
        pass

def group_membership(username, request):
    user = DBSession.query(User).get(username)
    perms = []
    if user:
        if user.is_owner:
            perms += ['group:admin']
        if user.is_dwg or user.is_admin:
            perms += ['group:dwg']
    return perms
