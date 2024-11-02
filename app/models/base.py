from datetime import datetime
from sqlmodel import Field, SQLModel


class Base(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # class Config:
    #    arbitrary_types_allowed = True
