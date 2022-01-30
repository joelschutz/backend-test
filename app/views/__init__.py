from pathlib import Path
from jinja2 import Environment
from fastapi.templating import Jinja2Templates

from app.settings import settings

class TemplateRender:
    # env: Environment = settings.JINJA_ENV
    template_ext = '.html'
    templates = Jinja2Templates(directory='app/templates')

    @classmethod
    def _render(cls, template_name: str, request, **kwargs):
        if not template_name.endswith(cls.template_ext):
            template_name += cls.template_ext

        kwargs.update({'request': request})

        return cls.templates.TemplateResponse(template_name, kwargs)

    @classmethod
    def render_login_page(cls, request, **kwargs):
        return cls._render('auth/login', request, **kwargs)
    
    @classmethod
    def render_signup_page(cls, request, **kwargs):
        return cls._render('users/register', request, **kwargs)

    @classmethod
    def render_score_page(cls, request, **kwargs):
        return cls._render('general_pages/homepage', request, **kwargs)
