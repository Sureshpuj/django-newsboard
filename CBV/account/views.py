from django.views.generic import *
from django.contrib.auth.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import *
class Index(TemplateView):
    template_name ='account/index.html'
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('login')
    
class LoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')

class LogoutView(LogoutView):
    next_page = reverse_lazy('index')  