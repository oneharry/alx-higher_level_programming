#!/usr/bin/python3
"""Module definition of a class State
    cities of that state
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """
        Definition of state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
