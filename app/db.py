from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import create_async_engine

SQLALCHEMY_URI: str = "mysql+pymysql://root:root@db:3306/sqlmodel_example?charset=utf8mb4"
ASYNC_SQLALCHEMY_URI: str = "mysql+aiomysql://root:root@db:3306/sqlmodel_example?charset=utf8mb4"

async_engine = create_async_engine(ASYNC_SQLALCHEMY_URI)
engine = create_engine(SQLALCHEMY_URI)
session = scoped_session(sessionmaker(engine))
