from fastapi import FastAPI
from router import uber
from router import get_hello


app = FastAPI()
app.include_router(uber.router)
app.include_router(get_hello.router)

