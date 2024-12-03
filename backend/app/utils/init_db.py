import sys
import os
import asyncio
from app.utils.database import engine
from app.models.base import Base
from app.models.user import User

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


async def init_db():
    async with engine.begin() as conn:
        # 既存のテーブルを削除したい場合はコメントを外す
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
