from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import LoginForm
from .models import ApplicationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    # if request.method == 'POST':
    #     # form = RegisterForm(request.POST)
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = User.objects.create_user(username=username, password=password)
    #
    #     user.save();
    #     print('user created')
    #     return redirect('bankapp:login')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        auth.login(request, user)
        return redirect('bankapp:login')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # authenticate the user
            # log the user in, etc.
            return redirect('bankapp:newbutton')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def newbutton(request):
    return render(request, 'newbutton.html')


def form(request):
    if request.method == 'POST':
        # Process the form submission here
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account = request.POST['account']
        materials = request.POST['materials']
        forms = ApplicationForm(name=name, dob=dob, age=age, gender=gender, phone=phone,
                     email=email, address=address, district=district, branch=branch,
                     account=account, materials=materials)

        forms.save()
        print('form created')
        messages.info(request,"application accepted")
    return render(request, 'form.html')
