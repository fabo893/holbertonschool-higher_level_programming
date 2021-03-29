#!/usr/bin/python3
"""
    List all State objects that contain the letter a
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    let_a = session.query(State).filter(State.name.like('%a%'))

    for x in let_a:
        print("{}: {}".format(x.id, x.name))

    session.close()
