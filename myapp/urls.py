from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logup/', views.logup, name='logup'),
    path('cart/', views.cart, name='cart'),
    path('iphone/', views.iphone, name='iphone'),
    path('samsung/', views.samsung, name='samsung'),
    path('oppo/', views.oppo, name='oppo'),
    path('nokia/', views.nokia, name='nokia'),
    path('google/', views.google, name='google'),
    path('add/', views.add, name='add'),
    path('del/', views.delete, name='del'),
    path('update/', views.update, name='update'),
    path('bill/', views.pay, name='bill'),
    path('logout/', views.logout, name="logout"),
]