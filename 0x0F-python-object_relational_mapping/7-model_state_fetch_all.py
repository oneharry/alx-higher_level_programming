#!/usr/bin/python3
"""Module definition of a class State
    cities of that state
"""

from sqlalchemy import create_engine, sessionmaker
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for s in session.query(State).order_by(State.id):
        print("{}: {}".format(s.id, s.name))
