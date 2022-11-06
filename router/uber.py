from typing import Optional
from fastapi import APIRouter, status, Response


router = APIRouter(
    prefix='/companies',
    tags=['uber']
)


@router.get('/login', status_code=status.HTTP_200_OK)
def create_employee(mail: str, password: str, response: Response):
    email = 'pierre@palenca.com'
    passwordd = 'MyPwdChingon123'
    """
    Simulates incorrect username or password
    """
    if ((mail not in email) and (password not in passwordd)):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'CREDENTIALS_INVALID', 'details': f'Incorrect username or password'}
    else:
        response.status_code = status.HTTP_200_OK
    return  {'message': f'SUCCESS', 'Access Token': f'cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5'}




@router.get('/user', status_code=status.HTTP_200_OK)
def get_employee_information(token: str, response: Response):
    access_token = 'cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5'
    """
    Simulates incorrect token
    """
    if token not in access_token:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'CREDENTIALS_INVALID', 'details': f'Incorrect token'}
    else:
        response.status_code = status.HTTP_200_OK
    return  {'message': f'SUCCESS',
            'platform': f"uber",
            'profile': f'...'}
