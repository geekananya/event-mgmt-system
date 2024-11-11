from django.urls import path
from . import views

urlpatterns = [
    path('get', views.get_users, name='getusers'),
    path('get/<int:pk>', views.get_user_by_id, name='getuser'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    # path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('logout', views.logout, name='logout'),
]