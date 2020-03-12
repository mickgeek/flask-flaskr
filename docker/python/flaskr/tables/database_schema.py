from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Post(Base):

    __tablename__ = 'posts'

    id = Column(Integer(), primary_key=True)
    title = Column(String(64))
    text = Column(String(256))
