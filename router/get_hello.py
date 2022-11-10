from typing import Optional
from fastapi import APIRouter, status, Response



router = APIRouter(
    prefix='/hello'
)


@router.post('/')
def create_hello():
    return "Hello Palenca"


