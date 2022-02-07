from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from app.views import TemplateRender
from app.controllers.auth import AuthController
from app.models.user import UserModel

router = APIRouter()

@router.get('/login', response_class=HTMLResponse)
def login_get(request: Request, user_info: dict=Depends(AuthController.auth_user_with_token)):
    # Redicts to /score page if the user is already logged in
    if isinstance(user_info, UserModel):
        return RedirectResponse('/score')
    
    response = TemplateRender.render_login_page(request, **user_info)
    if user_info.get('error_codes', [])[0] == 1:
        response.delete_cookie('access_token')

    return response

@router.post('/login', response_class=HTMLResponse)
def login_post(request: Request, user_info: dict=Depends(AuthController.auth_user_with_credentials)):
    # Redicts to /score page if the user is already logged in
    if isinstance(user_info, UserModel):
        response = RedirectResponse('/score', status_code=302)
        response.set_cookie('access_token', AuthController.create_token(user_info))

        return response

    return TemplateRender.render_login_page(request, **user_info)

@router.get('/logout', response_class=HTMLResponse)
def logout_get(request: Request, user_info: dict=Depends(AuthController.auth_user_with_token)):
    # Redicts to /score page if the user is already logged in
    response = RedirectResponse('/login')

    if isinstance(user_info, UserModel) or user_info.get('error_codes', [])[0] == 1:
        response.delete_cookie('access_token')

    return response
