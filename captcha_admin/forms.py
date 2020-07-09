from django.contrib.admin.forms import (
    AdminAuthenticationForm as _AdminAuthenticationForm
)
from django.contrib.auth.forms import AuthenticationForm as _AuthenticationForm
from captcha.fields import ReCaptchaField


class AdminAuthenticationForm(_AdminAuthenticationForm):
    captcha = ReCaptchaField()


class AuthenticationForm(_AuthenticationForm):
    captcha = ReCaptchaField()