from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:shortened_url>', views.redirect_me, name='redirect_me')
]
