from django.conf.urls import url
from .views import home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url('home$', home, name="player_home"),
    url('login$', LoginView.as_view(template_name="player/login_form.html"),
        name="player_login"),
    url('logout', LogoutView.as_view(),
        name="player_logout")
]