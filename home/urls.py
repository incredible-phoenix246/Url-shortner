from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="name"),
    path('<str:short_code>/', views.redirect_to_long_url, name='redirect_to_long_url'),
]




