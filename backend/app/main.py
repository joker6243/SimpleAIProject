from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI()

# ユーザー関連のルートを登録
app.include_router(user_router)


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

