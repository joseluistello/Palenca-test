from typing import Optional
from fastapi import APIRouter, status, Response



router = APIRouter(
    prefix=''
)


@router.get('/')
def create_hello():
    return "Hello Palenca"


