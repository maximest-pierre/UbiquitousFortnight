from django.conf.urls import url
from authentication.forms import LoginForm
from django.contrib.auth import views as auth_views
from authentication.views import UserCreateView

app_name = "authentication"

urlpatterns =[
    url(r'^$', auth_views.login, {'template_name': 'system/login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^register/$', UserCreateView.as_view(), name="register"),
]