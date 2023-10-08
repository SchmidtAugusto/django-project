from django.urls import path
from app_user_singup import views

urlpatterns = [
    # rota, view responsável, nome de ref.
    path('', views.home, name = 'home'),
    path('users/', views.users, name = 'listing_users')
]
