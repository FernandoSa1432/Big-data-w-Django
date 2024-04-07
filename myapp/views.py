from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

#Esto es para que al autenticar que el usuario si existe lo redirija a la pagina principal
class CustomLoginView(LoginView):
    def form_valid(self, form):
        super().form_valid(form)
        return redirect('main_page')
    


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login_view(request):
    return LoginView.as_view(template_name='login.html')(request)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register_user.html', {'form':form})

def main_page_view(request):
    return render(request, 'main_page.html')