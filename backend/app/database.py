from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE = 'mysql+pymysql://root:1234@0.0.0.0:3307/fastapi'

engine = create_engine(DATABASE, echo=True)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()   # 실제 연결
Base.query = SessionLocal.query_property()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()