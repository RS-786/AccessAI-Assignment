from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import  authenticate, login as auth_login, logout, decorators, models
from .forms import SignupForm, EmployeeForm
from .models import Employee
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "employee/index.html")

def read(request, start_from):
    employees = Employee.objects.all()
    count = employees.count()

    if start_from >= count:
        employees = []

    elif start_from + 5 >= count-1:
        employees = employees[start_from:count]

    else:
        employees = employees[start_from:start_from + 5]

    context = {
        'employees': employees,
        'next': start_from + 5,
        'prev': start_from - 5
    }
    return render(request, "employee/read.html", context=context)


@decorators.login_required
def create(request):
    form = EmployeeForm
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee Creation Successful')
            return redirect('index')
        else:
            context = {
                'form': form
            }
            return render(request, "employee/create.html", context = context)

    else:
        context = {
            'form' : form
        }
        return render(request, "employee/create.html", context = context)


@decorators.login_required
def search(request, view):
    if request.method == "POST":
        name = request.POST['name']
        emp = Employee.objects.filter(name=name).first()
        if emp is None:
            context = {
                "message": "Employee not found !",
                "url": "/" + view + "/search"
            }
            return render(request, "employee/search.html", context=context)

        else:
            context = {
                "url" : "/update/" + emp.name,
                "name": emp.name,
                "gender": emp.gender,
                "salary": emp.salary,
                "address": emp.address,
                "form" : EmployeeForm
            }
            return render(request, "employee/update.html", context=context)

    else:
        if view == "search":
            context = {
                "url": "/search/search"
            }
        else:
            context = {
                "url" : "/" + view
            }
        return render(request,"employee/search.html",context=context)


def update(request, name):

    if request.method == "POST":
        instance = Employee.objects.get(name = name)
        form = EmployeeForm(instance = instance,data = request.POST)

        if(form.is_valid()):
            form.save()
            messages.success(request, 'Information Updated Successfully')
            return redirect('index')

        else:
            context = {

            }
            return render(request,"employee/update.html",context = context)



def delete(request):

    if request.method == "POST":
        name = request.POST['name']
        emp = Employee.objects.filter(name = name).first()

        if emp is None:
            context = {
                "message" : "Employee not found !",
                "url" : "/delete"
            }
            return render(request, "employee/search.html", context=context)

        else:
            emp.delete()
            messages.success(request, 'Employee was Deleted')
            return redirect('index')


def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            User = models.User
            username = form.cleaned_data['username']
            exists = User.objects.filter(username__contains=username)

            if exists:
                context = {'message': 'Username is taken !'}
                return render(request, "registration/register.html", context)

            else:
                password = form.cleaned_data['password']
                user = User.objects.create_user(username=username, password=password)
                auth_login(request,user)
                return redirect('index')

    else:
        context = {'message': ''}
        return render(request, "registration/register.html", context=context)

def login(request):
    form = SignupForm
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                context = {'message': 'Wrong username or password !',
                           'form' : form}
                return render(request, "registration/login.html", context = context)

            else:
                auth_login(request, user)
                return redirect('index')

        else:
            context = {
                'form': form
            }
            return render(request, "registration/login.html", context = context)

    else:
        context = {
            'form': form
        }
        return render(request, "registration/login.html", context = context)


def loggedout(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect('index')