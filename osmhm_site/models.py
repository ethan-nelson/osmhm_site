from sqlalchemy import (
    Column,
    Index,
    Integer,
    BigInteger,
    Text,
    Float,
    Boolean,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.hybrid import (
    hybrid_property
)

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class History(Base):
    __tablename__ = 'history_all_changesets'
    id = Column(Integer, primary_key=True, nullable=False)
    changeset = Column(Text, nullable=False)
    username = Column(Text, nullable=False)
    timestamp = Column(Text, nullable=False)
    created = Column(Text)
    modified = Column(Text)
    deleted = Column(Text)

class History_Filters(Base):
    __tablename__ = 'history_filters'
    id = Column(Integer, primary_key=True, nullable=False)
    flag = Column(Integer, nullable=False)
    username = Column(Text, nullable=False)
    changeset = Column(BigInteger, nullable=False)
    timestamp = Column(Text, nullable=False)
    quantity = Column(Text, nullable=False)

class Watched_Users(Base):
    __tablename__ = 'watched_users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(Text, nullable=False)
    reason = Column(Text)
    author = Column(Text)
    email = Column(Text)

class History_Users(Base):
    __tablename__ = 'history_users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(Text, nullable=False)
    changeset = Column(BigInteger, nullable=False)
    timestamp = Column(Text, nullable=False)
    created = Column(BigInteger)
    modified = Column(BigInteger)
    deleted = Column(BigInteger)

class Watched_Objects(Base):
    __tablename__ = 'watched_objects'
    id = Column(Integer, primary_key=True, nullable=False)
    element = Column(Text, nullable=False)
    reason = Column(Text)
    author = Column(Text)
    email = Column(Text)

class History_Objects(Base):
    __tablename__ = 'history_objects'
    id = Column(Integer, primary_key=True, nullable=False)
    element = Column(Text, nullable=False)
    username = Column(Text, nullable=False)
    changeset = Column(BigInteger, nullable=False)
    timestamp = Column(Text, nullable=False)
    action = Column(Text)

class Watched_Keys(Base):
    __tablename__ = 'watched_keys'
    id = Column(Integer, primary_key=True, nullable=False)
    key = Column(Text, nullable=False)
    value = Column(Text, nullable=False)
    reason = Column(Text)
    author = Column(Text)
    email = Column(Text)

class History_Keys(Base):
    __tablename__ = 'history_keys'
    id = Column(Integer, primary_key=True, nullable=False)
    key = Column(Text, nullable=False)
    value = Column(Text, nullable=False)
    username = Column(Text, nullable=False)
    changeset = Column(BigInteger, nullable=False)
    timestamp = Column(Text, nullable=False)
    action = Column(Text)

class File_List(Base):
	__tablename__ = 'file_list'
	id = Column(Integer, primary_key=True, nullable=False)
	sequence = Column(Text)
	timestamp = Column(Text)
	timetype = Column(Text)
	read = Column(Boolean)

class Whitelisted_Users(Base):
    __tablename__ = 'whitelisted_users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(Text, nullable=False)
    reason = Column(Text)
    author = Column(Text)

MEMBER = 1
DWGMEMBER = 2
ADMIN = 3
OWNER = 4

class User(Base):
    __tablename__ = 'registered_users'
    id = Column(BigInteger, primary_key=True)
    username = Column(Text)
    role_member = MEMBER
    role_dwg = DWGMEMBER
    role_admin = ADMIN
    role_owner = OWNER
    role = Column(Integer)

    def __init__(self, id, username):
        self.id = id
        self.username = username

    @hybrid_property
    def is_owner(self):
        return self.role is self.role_owner

    @hybrid_property
    def is_admin(self):
        return self.role is self.role_admin

    @hybrid_property
    def is_dwg(self):
        return self.role is self.role_dwg


class UnblockedUsers(Base):
    __tablename__ = 'unblocked_users'
    id = Column(BigInteger, primary_key=True)
    username = Column(Text)
    date_expired = Column(Text)

class BlockedUsers(Base):
    __tablename__ = 'blocked_users'
    id = Column(BigInteger, primary_key=True)
    blockee = Column(Text)
    blocked = Column(Text)
    begindate = Column(Text)
    enddate = Column(Text, nullable=True)
    reason = Column(Text)

#Index('history_index', History_Filters.id, unique=True)
#Index('users_index', Watched_Users.id, unique=True)
#Index('user_history_index', History_Users.id, unique=True)
#Index('objects_index', Watched_Objects.id, unique=True)
#Index('object_history_index', History_Objects.id, unique=True)
#Index('whitelist_index', Whitelisted_Users.id, unique=True)
#Index('unblocked_user_index', UnblockedUsers.id, unique=True)
#Index('blocked_user_index', BlockedUsers.id, unique=True)
