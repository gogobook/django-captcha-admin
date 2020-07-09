from django.contrib.auth.views import LoginView as _LoginView

from captcha_admin.forms import AuthenticationForm

class LoginView(_LoginView):
    form_class = AuthenticationForm
``