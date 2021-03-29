#!/usr/bin/python3
"""
    Print all City objects
"""


from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for x in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({}) {}".format(x.State.name, x.City.id, x.City.name))

    session.close()
