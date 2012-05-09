from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///db/storage.db', convert_unicode=True, echo=True)
dbsession = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
DeclarativeBase = declarative_base()
DeclarativeBase.query = dbsession.query_property()
metadata = DeclarativeBase.metadata


def init_db(engine):
    DeclarativeBase.metadata.create_all(bind=engine)

# Put your models here


# import your models.
from models.auth import Group, Permission, User