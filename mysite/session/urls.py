from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views

app_name = "session"
urlpatterns = [
    path("cookie", views.cookie),
    path("theme", views.theme_switcher, name="theme_switcher"),
    path("sessfun", views.sessfun, name="sessfun"),
    path("card", views.inc_dec_card, name="card"),
]
