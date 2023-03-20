#!/usr/bin/python3
"""Module prints the state object with name passed as argument
   from database
"""

from sqlalchemy import create_engine
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

    s = session.query(State).filter(State.name == sys.argv[4]).first()
    if (s):
        print("{}".format(s.id))
    else:
        print("Not found")
