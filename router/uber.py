from fastapi import APIRouter, status, Response
from pydantic import BaseModel

router = APIRouter(
    prefix='/uber',
    tags=['uber']
)


class CreateEmployeeParams(BaseModel):
    email: str
    password: str


@router.post('/login')
def create_employee(params: CreateEmployeeParams, response: Response):
    email = params.email
    password = params.password

    if email != 'pierre@palenca.com' or password != 'MyPwdChingon123':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {'error': f'CREDENTIALS_INVALID', 'details': f'Incorrect username or password'}

    return {
        "message": "SUCCESS",
        "platform": "uber",
        "profile": {
            "country": "mx",
            "city_name": "Ciudad de Mexico",
            "worker_id": "34dc0c89b16fd170eba320ab186d08ed",
            "first_name": "Pierre",
            "last_name": "Delarroqua",
            "email": "pierre@palenca.com",
            "phone_prefix": "+52",
            "phone_number": "5576955981",
            "rating": "4.8",
            "lifetime_trips": 1254
        }
    }


@router.get('/profile/{access_token}')
def get_employee_information(access_token: str, response: Response):
    if access_token != 'cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {'error': f'CREDENTIALS_INVALID', 'details': f'Incorrect token'}

    return {
        "message": "SUCCESS",
        "access_token": "cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5"
        }
