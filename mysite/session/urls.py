from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views

app_name = "session"
urlpatterns = [
    # path('', TemplateView.as_view(template_name='home/main.html')),
    # path('sessfun', sessfun, 'sessfun'),
    path("cookie", views.cookie),
    path("theme", views.theme_switcher, name="theme_switcher"),
]
