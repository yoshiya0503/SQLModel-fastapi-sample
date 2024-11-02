from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel, select
from sqlalchemy.orm import selectinload
from app.db import engine
from app.context import ContextDep
from app.models import User, BettingHistory


@asynccontextmanager
async def lifespan(_: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


class UserResponse(SQLModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None
    full_name: str | None = None
    betting_histories: list[BettingHistory] = []


@app.get("/list", response_model=list[UserResponse])
async def list(context: ContextDep):
    query = select(User).options(selectinload(User.betting_histories))
    users = (await context.session.scalars(query)).all()
    return users


@app.get("/create")
async def create(context: ContextDep):
    user = User(name="other", email="other@other.com", password="password")
    user.betting_histories += [
        BettingHistory(point=1, reward=1, histories=[{"key": "value"}]),
        BettingHistory(point=2, reward=2, histories=[{"key": "value"}]),
        BettingHistory(point=3, reward=3, histories=[{"key": "value"}, {"key": "value"}]),
    ]
    context.session.add(user)
    return {"status": "ok"}
