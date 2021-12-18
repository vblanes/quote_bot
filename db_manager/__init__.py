from models import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Documentation says that this only had to be created one time in the app
# And suggests to sep up this in __init__ file within the package
# However IDK who that really works in a small app like these so by the moment
# We would only use one instance of this class. Possible solutions:
# 1) Make this class as singletone
# 2) Figure out how to use the __init__ file properly
# ----> Solution chosen here
# source: https://docs.sqlalchemy.org/en/13/orm/session_basics.html
Session = sessionmaker()
engine = create_engine('sqlite:///quotes.sqlite')
Session.configure(bind=engine)
# Create the tables
# TODO que pasa si ya existen??
Base.metadata.create_all(engine)