from fastapi import APIRouter


router = APIRouter(
    prefix='/hello'
)


@router.get('/')
def create_hello():
    return "Hello Palenca"
