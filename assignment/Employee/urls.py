from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.signup, name='signup'),
    path("login", views.login, name = 'login'),
    path("loggedout", views.loggedout, name = 'logout'),
    path("", views.index, name = 'index'),
    path("read/<int:start_from>",views.read,name='read'), # start_from variable is used for implementing pagination
    path("create",views.create,name = 'create'),
    path("update/<str:name>",views.update,name = 'update'), # name variable is used for updating specific employee
    path("delete",views.delete,name = 'delete'),
    path("search/<str:view>",views.search,name = 'search') # view variable tells whether to delete or update after searching
]