from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.signup, name='signup'),
    path("login", views.login, name = 'login'),
    path("loggedout", views.loggedout, name = 'logout'),
    path("", views.index, name = 'index'),
    path("read/<int:start_from>",views.read,name='read'),
    path("create",views.create,name = 'create'),
    path("update",views.update,name = 'update'),
    path("delete",views.delete,name = 'delete'),
]