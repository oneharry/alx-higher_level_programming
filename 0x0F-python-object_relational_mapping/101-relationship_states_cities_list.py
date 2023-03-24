#!/usr/bin/python3
"""Module lists all State and CIty objects in db 'hbtn_0e_usa'
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base
import sys

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for s in session.query(State).order_by(State.id).all():
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("\t{}: {}".format(c.id, c.name))
