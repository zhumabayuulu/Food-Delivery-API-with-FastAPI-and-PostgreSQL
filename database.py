from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('postgresql://postgres:lokiloki@localhost/deliveri',
                       echo=True)

Base = declarative_base()
session = sessionmaker()

