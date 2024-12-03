from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# データベースURLの設定（適宜変更してください）
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

# 非同期エンジンを作成
engine = create_async_engine(DATABASE_URL, echo=True)

# セッションローカルを作成
async_session = sessionmaker(bind=engine, class_=AsyncSession, 
                             expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session
