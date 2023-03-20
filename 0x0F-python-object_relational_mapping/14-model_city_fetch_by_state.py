#!/usr/bin/python3
"""Module deletes all states objects containing letter a
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
import sys

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for c, s in session.query(City, State).filter(City.state_id ==
                                                  State.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
