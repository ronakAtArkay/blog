from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = "mysql+mysqlconnector://root:%s@localhost:3306/blog" % quote("Arkay@210")

engine = create_engine(url)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
