#!/usr/bin/python3
"""A script lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco", state_id = new_state.id)
    session.add(new_state)
    session.commit()
    session.close()
