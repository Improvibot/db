import logging
from sqlalchemy     import create_engine
from sqlalchemy.orm import Session

from db.models      import Base, Song, User, Queue


class Database:
    def __init__(self, database='sqlite+pysqlite:///../db/improvibot.db'):
        self.engine = create_engine(database, echo=True)
        logging.info(Base.metadata)
        Base.metadata.create_all(self.engine)

    def save(self, db_object):
        with Session(self.engine) as session:
            session.add(db_object)
            session.commit()

