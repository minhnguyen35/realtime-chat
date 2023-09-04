from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .form import LoginForm, RegisterForm
from .CreateNewUserUseCase import CreateNewUserUseCase
from .VerifyLoginUseCase import VerifyLoginUseCase
from .constants import DB_Status

# Create your views here.
def login(request: HttpRequest):
    if 'email' in request.session:
        return redirect('mainApp:homepage')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            status = VerifyLoginUseCase().execute(data['email'], data['password'])
            if status == DB_Status.SUCCESS:
                request.session['email'] = data['email']
                return redirect('mainApp:homepage')
            elif status == DB_Status.WRONG_PASSWORD or status == DB_Status.NOT_FOUND:
                form.add_error('email', 'Your email or password is incorrect.')
                form.add_error('password', 'Your email or password is incorrect.')
            return render(request, "authentication/login.html", {'form': form})
                
    return render(request, "authentication/login.html", {'form': LoginForm(None)})

def logout(request: HttpRequest):
    del request.session['email']
    return redirect('mainApp:index')

def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # print("valid form ", data)
            status = CreateNewUserUseCase().execute(data['email'], data['user_name'], data['password'])
            if status == DB_Status.SUCCESS:
                return redirect('authentication:login')
            if status == DB_Status.ALREADY_EXIST:
                form.add_error('email',"Account already exists!")
            elif status == DB_Status.INTERNAL_ERROR:
                form.add_error('email',"Internal error!")
            return render(request, 'authentication/register.html', {'form': form})
        else:
            print("invalid form")
            return render(request, 'authentication/register.html', {'form': form})
    return render(request, 'authentication/register.html', {'form': RegisterForm(None)})