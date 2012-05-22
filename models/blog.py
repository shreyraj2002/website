#SQL Alchemy Model for Blog

#Imports Needed:
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship, synonym
from sqlalchemy.types import DateTime, Integer, Unicode
from models import dbsession, DeclarativeBase, metadata


#{ Association tables
# This is the association table for the many-to-many relationship between groups and members.
user_group_table = Table('user_group', metadata, 
    Column('user_id', Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)

# This is the association table for the many-to-many relationship between groups and permissions.
group_permission_table = Table('group_permission', metadata,
    Column('group_id', Integer, ForeignKey('groups.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)
