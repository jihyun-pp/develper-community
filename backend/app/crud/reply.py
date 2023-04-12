from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from datetime import datetime

import app.schema.schemas as schema
from app.model import Board, User, Reply

async def get_replys(bid: int, db: AsyncSession):
    return db.query(Reply).filter(Reply.bid == bid).order_by(Reply.rid).all()

async def insert_reply(bid: int, uid: int, _reply: schema.InsertReply, db: AsyncSession):
    try:
        add_reply = Reply(
            bid=bid,
            uid=uid,
            reply=_reply.reply,
            createdAt=datetime.now(),
            updatedAt=datetime.now()
        )
        db.add(add_reply)
        await db.commit()

    except Exception as e:
        return e
    return "S"