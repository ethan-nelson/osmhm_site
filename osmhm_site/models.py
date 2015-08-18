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
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    timestamp = Column(Text)
    changeset = Column(Integer)
    username = Column(Text)
    flag = Column(Integer)
    quantity = Column(Float)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text)
    reason = Column(Text)
    author = Column(Text)
    email = Column(Text)

class UserHistory(Base):
    __tablename__ = 'user_history'
    id = Column(Integer, primary_key=True)
    timestamp = Column(Text)
    changeset = Column(Integer)
    username = Column(Text)
    added = Column(Float)
    changed = Column(Float)
    deleted = Column(Float)

class Objects(Base):
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True)
    number = Column(Text)
    note = Column(Text)
    author = Column(Text)
    email = Column(Text)

class ObjectHistory(Base):
    __tablename__ = 'object_history'
    id = Column(Integer, primary_key=True)
    timestamp = Column(Text)
    changeset = Column(Integer)
    username = Column(Text)
    action = Column(Text)
    objectid = Column(Text)

class Filetime(Base):
	__tablename__ = 'filetime'
	id = Column(Integer, primary_key=True)
	sequencenumber = Column(Text)
	timestamp = Column(Text)
	readflag = Column(Boolean)

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

class Whitelist(Base):
    __tablename__ = 'whitelist'
    id = Column(BigInteger, primary_key=True)
    username = Column(Text)
    reason = Column(Text)
    author = Column(Text)

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

Index('history_index', History.id, unique=True)
Index('users_index', Users.id, unique=True)
Index('user_history_index', UserHistory.id, unique=True)
Index('objects_index', Objects.id, unique=True)
Index('object_history_index', ObjectHistory.id, unique=True)
Index('whitelist_index', Whitelist.id, unique=True)
Index('unblocked_user_index', UnblockedUsers.id, unique=True)
Index('blocked_user_index', BlockedUsers.id, unique=True)
