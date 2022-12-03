from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote

url = ("mysql+mysqlconnector://root:%s@localhost:3306/blog" % quote("Arkay@210"))

engine = create_engine(url)

sessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()