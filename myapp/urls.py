from django.urls import path
#El utilizar ese punto significa que importa desde el archivo actual. en este caso myapp
from .views import CustomLoginView, home, register_view, main_page_view


urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register_view, name='register'),
    path('main_page/', main_page_view, name='main_page')
    #Aqui se agregan mas urls para la aplicacion
]