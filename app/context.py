from typing import Annotated
from fastapi import HTTPException, Depends
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_engine


@dataclass
class Context:
    session: AsyncSession


async def context():
    async with AsyncSession(async_engine) as session:
        context = Context(session=session)
        context.session = session
        try:
            yield context
        except HTTPException:
            await session.rollback()
            raise
        except Exception:
            await session.rollback()
            raise
        else:
            await session.commit()
        finally:
            await session.close()


ContextDep = Annotated[Context, Depends(context)]
