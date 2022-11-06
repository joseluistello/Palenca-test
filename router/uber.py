from typing import Optional
from fastapi import APIRouter, status, Response


router = APIRouter(
    prefix='/companies'
)


@router.get('/login', status_code=status.HTTP_200_OK)
def create_employee(mail: str, password: str, response: Response):
    email = 'pierre@palenca.com'
    passwordd = 'MyPwdChingon123'
    """
    Simulates tocken autentication
    """
    if ((mail not in email) and (password not in passwordd)):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'CREDENTIALS_INVALID details: Incorrect username or password'}
    else:
        response.status_code = status.HTTP_200_OK
    return  {'message': f'SUCCESS Access Token: cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5'}
