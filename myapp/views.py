from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task

# Create your views here.

def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    return HttpResponse('Holiiii watafoc is dis ma boi?, este es el user %s' % username)

def about(request):
    return HttpResponse("About")


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe = False)

def tasks(request, id):
    #El primer id es el propiedad de la clase y el segundo es la propiedad de la funcion
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)