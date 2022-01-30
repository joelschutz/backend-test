from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from app.views import TemplateRender
from app.controllers.auth import AuthController
from app.models.user import UserModel
from app.settings import settings

router = APIRouter()

@router.get('/score', response_class=HTMLResponse)
def score_get(request: Request, user_info: dict=Depends(AuthController.auth_user_with_token)):
    # Redicts to /login page if the user is not logged in
    if not isinstance(user_info, UserModel):
        return RedirectResponse('/login')

    base_url = settings.HOST

    if settings.PORT != 80:
        base_url += f':{settings.PORT}'

    params = {
        'user': user_info,
        'base_url': base_url
    }

    return TemplateRender.render_score_page(request, **params)
