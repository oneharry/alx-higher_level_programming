#!/usr/bin/python3
"""Module definition of a class State
    cities of that state
"""

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

db_url = 'sqlite:///db.sqlite'
engine = create_engine(db_url)

Base = declarative_base()


class State:
    """
        Definition of state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
