from typing import Optional
from fastapi import APIRouter, Depends, Query, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from app.controllers.users import UserController

from app.views import TemplateRender
from app.controllers.auth import AuthController
from app.models.user import UserModel

router = APIRouter()

@router.get('/signup', response_class=HTMLResponse)
def signup_get(
    request: Request,
    user_info: dict=Depends(AuthController.auth_user_with_token),
    inviter: Optional[str] = Query(None)
):
    # Redicts to /score page if the user is already logged in
    if isinstance(user_info, UserModel):
        return RedirectResponse('/score')
    
        
    if user_info.get('error_codes', [])[0] == 1:
        response = RedirectResponse('/login')
        response.delete_cookie('access_token')

        return response

    if inviter:
        user_info.update({'inviter': inviter})

    return TemplateRender.render_signup_page(request, **user_info)

@router.post('/signup', response_class=HTMLResponse)
def signup_post(
    request: Request,
    inviter: Optional[str] = Form(None),
    email: str = Form(...),
    name: str = Form(...),
    phone: str = Form(...),
    password: str = Form(...)
):
    new_data = {}

    new_data['email'] = email
    new_data['name'] = name
    new_data['phone'] = phone
    new_data['password'] = password

    user_info = UserController.create_if_new(new_data)


    if isinstance(user_info, UserModel):
        if inviter:
            UserController.increment_score(inviter)

        response = RedirectResponse('/score', status_code=302)
        response.set_cookie('access_token', AuthController.create_token(user_info))

        return response

    return TemplateRender.render_signup_page(request, **user_info)