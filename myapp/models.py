from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Project(models.Model):
    name =  models.CharField(max_length = 200)


class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class CustomUser(AbstractUser):
    #Podemos agregar campos personalizados aqui en caso de que sea necesario
    pass

    class Meta:
        app_label = 'myapp'

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank = True,
        related_name='custom_user_groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank = True,
        related_name='custom_user_permissions'
    )