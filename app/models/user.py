from typing import TYPE_CHECKING
from sqlmodel import Relationship
from pydantic import computed_field
from app.models.base import Base

if TYPE_CHECKING:
    from app.models.betting_history import BettingHistory


class Meta:
    def debug(self):
        print(self.__tablename__)


class User(Base, Meta, table=True):
    """
    ユーザーモデル
    """

    __tablename__ = "users"  # type: ignore

    name: str | None = None
    email: str | None = None
    password: str | None = None

    @computed_field
    @property
    def full_name(self) -> str:
        return f" your full name {self.name}"

    betting_histories: list["BettingHistory"] = Relationship(back_populates="user")
