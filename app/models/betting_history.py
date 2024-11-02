from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Column, Relationship
from sqlalchemy import JSON
from app.models.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class BettingHistory(Base, table=True):
    """
    ユーザーモデル
    """

    __tablename__: str = "betting_histories"  # type: ignore

    user_id: int | None = Field(default=None, foreign_key="users.id")
    point: int = 0
    reward: int = 0

    histories: list[dict] = Field(default_factory=list, sa_column=Column(JSON))
    user: Optional["User"] = Relationship(back_populates="betting_histories")
