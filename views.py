
from django.shortcuts import render, redirect
from .models import Employee
from .forms import SignUpForm, LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Employee.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect('home') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = Employee.objects.create(username=username, email=email, password=password)
            request.session['user_id'] = user.id
            return redirect('home') 
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def home(request):
    return render(request,'home.html')
def logout(request):
    request.session.clear()
    return redirect('login')  

