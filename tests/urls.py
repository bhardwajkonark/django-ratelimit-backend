from django.urls import re_path
from ratelimitbackend import admin
from ratelimitbackend.views import login

from .forms import CustomAuthForm, TokenOnlyAuthForm


urlpatterns = [
    re_path(r'^login/$', login, {'template_name': 'admin/login.html'}, name='login'), # noqa
    re_path(r'^custom_login/$', login, {'template_name': 'custom_login.html','authentication_form': CustomAuthForm},name='custom_login'), # noqa
    re_path(r'^token_login/$', login, {'template_name': 'token_only_login.html','authentication_form': TokenOnlyAuthForm},name='token_only_login'), # noqa
    re_path(r'^admin/', admin.site.urls),
            ] # noqa
