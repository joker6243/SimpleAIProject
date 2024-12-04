from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# SQLiteデータベースURL
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# エンジンの作成
engine = create_async_engine(DATABASE_URL, echo=True)

# セッション作成
async_session = sessionmaker(bind=engine, class_=AsyncSession, 
                             expire_on_commit=False)


# 非同期データベースセッション取得関数
async def get_db():
    async with async_session() as session:
        yield session