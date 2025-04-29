from django.urls import path
from .views import *
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]