import asyncio
from app.utils.database import engine
from app.models.base import Base
from app.models.user import User


async def init_db():
    # テーブルの登録を明示
    models = [User]
    print("Initializing tables for models:")
    for model in models:
        print(f"- {model.__tablename__}")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())

