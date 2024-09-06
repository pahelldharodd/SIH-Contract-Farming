from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL='mysql+pymysql://root:Root@123@localhost:3306/mydatabase'
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root%40123@localhost:3306/sih"




engine= create_engine(SQLALCHEMY_DATABASE_URL)
 
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base= declarative_base()

