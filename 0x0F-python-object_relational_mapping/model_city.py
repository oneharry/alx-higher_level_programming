#!/usr/bin/python3
"""Module definition of a class City
"""

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from model_state import Base


class City(Base):
    """
        Definition of City
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
