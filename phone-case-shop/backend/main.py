from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Phone Case Shop API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    {
        "id": 1,
        "name": "몬치치 케이스",
        "price": 15000,
        "emoji": "🐵"
    },
    {
        "id": 2,
        "name": "키티 케이스",
        "price": 12000,
        "emoji": "🎀"
    },
    {
        "id": 3,
        "name": "짱구 케이스",
        "price": 13000,
        "emoji": "⭐"
    }
]


@app.get("/")
def root():
    return {"message": "핸드폰 케이스 쇼핑몰 Backend"}


@app.get("/products")
def get_products():
    return products