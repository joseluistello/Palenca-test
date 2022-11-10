from typing import Optional
from fastapi import APIRouter, status, Response



router = APIRouter(
    prefix=''
)


@router.post('/')
def create_hello():
    return "Hello Palenca"


