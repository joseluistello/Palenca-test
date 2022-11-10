from typing import Optional
from fastapi import APIRouter, status, Response


router = APIRouter(
    prefix='/uber',
    tags=['uber']
)


@router.post('/login', status_code=status.HTTP_200_OK)
def create_employee(mail: str, password: str, response: Response):
    email = 'pierre@palenca.com'
    passwordd = 'MyPwdChingon123'
    profile_information = {
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
    """
    Simulates incorrect username or password
    """
    if ((mail != email) or (password != passwordd)):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {'error': f'CREDENTIALS_INVALID', 'details': f'Incorrect username or password'}
    else:
        response.status_code = status.HTTP_200_OK
    return  profile_information




@router.get('/profile/{access_token}', status_code=status.HTTP_200_OK)
def get_employee_information(token: str, response: Response):
    access_token = 'cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5'
    success_information = {
   "message": "SUCCESS",
   "access_token": "cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5"
    }

    """
    Simulates incorrect token
    """
    if token != access_token:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {'error': f'CREDENTIALS_INVALID', 'details': f'Incorrect token'}
    else:
        response.status_code = status.HTTP_200_OK
    return  success_information
