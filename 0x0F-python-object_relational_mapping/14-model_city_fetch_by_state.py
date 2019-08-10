#!/usr/bin/python3
"""A script that deletes State objects with a name containing the letter a"""

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
    for row in session.query(State, City).join(City).order_by(City.id):
        print("{:}: ({:}) {:}".format(row[0].name, row[1].id, row[1].name))
    session.commit()
    session.close()
