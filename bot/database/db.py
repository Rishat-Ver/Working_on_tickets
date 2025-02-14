from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from dotenv import load_dotenv

import datetime
import os


load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')
Base = declarative_base()
engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Profession(Base):
    __tablename__ = "professions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    tickets = relationship("Ticket", back_populates="profession")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    keys = Column(String, nullable=False)
    link = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    hour = Column(Integer, nullable=False)
    profession_id = Column(Integer, ForeignKey("professions.id"))

    profession = relationship("Profession", back_populates="tickets")


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session():
    async with SessionLocal() as session:
        yield session
