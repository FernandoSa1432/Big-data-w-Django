from django.urls import path
#El utilizar ese punto significa que importa desde el archivo actual. en este caso myapp
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/<int:id>', views.tasks)
]