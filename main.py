import os

from app.web.app import setup_app
from aiohttp.web import run_app



if __name__ == "__main__":
    run_app(
        setup_app(
            config_path = "./config.yml"
        )
    )
    
    
"""
import asyncio

from sqlalchemy.orm import (
    declarative_base, 
    sessionmaker
)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)

from sqlalchemy import (
    Column,
    Integer,
    select,
    update,
    CHAR,
    insert
)

from sqlalchemy.engine import (
    ChunkedIteratorResult
)


DATABASE_URL = "postgresql+asyncpg://postgres:123456@0.0.0.0"

db = declarative_base()


class Tickets(db):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, autoincrement=0)
    ticket_no = Column(CHAR(13))

    def __repr__(self) -> str:
        return f"{self.ticket_no}"



Q1 = select(Tickets)

U1 = update(Tickets).where(Tickets.ticket_no == "DEADBABA").values(ticket_no = "first insert")
I1 = insert(Tickets).values(ticket_no = 'third insert')



async def async_main():
    engine = create_async_engine(DATABASE_URL, echo=False, future=True)
    async_session = sessionmaker(engine, expire_on_commit=False, class_= AsyncSession)
    
    
    ticket = Tickets(ticket_no = "thtasd")

    async with async_session() as session:
        session.add(ticket)
        await session.commit()

    await engine.dispose()


    #async with async_session() as session:
    #    res: ChunkedIteratorResult = await session.execute(Q1)
#
 #       for i in res:
 #           print(i)

    #await engine.dispose()



if __name__ == "__main__":
    asyncio.run(async_main())
"""