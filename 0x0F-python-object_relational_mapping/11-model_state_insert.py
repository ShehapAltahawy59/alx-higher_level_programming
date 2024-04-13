#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.bind = engine
    session = Session(engine)
    state = State(name='Louisiana')
    session.add(state)
    print(state.id)
    session.close()
