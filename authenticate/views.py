from django.shortcuts import redirect, render
from . models import account_data
from authenticate.models import Profile
from .forms import UserLoginForm
from django.contrib.sessions.models import Session
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
import json

# Create your views here.


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            getSessionOrAccountData(request, username)
            return redirect('shop:home')
        else:
            pass
    return render(request, 'authenticate/login.html')


def log_out(request):
    try:
        cart = request.session[settings.CART_SESSION_ID]
        key = request.session.session_key
        setSessionOrAccountData(request, key, cart)
        logout(request)
        return redirect('shop:home')
    except:
        logout(request)
        return redirect('shop:home')


def sign_in(request):
    if request.method == "POST":
        password = request.POST['password']
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        city = request.POST['city']
        address = request.POST['address']
        phone = request.POST['phone']
        user = User.objects.create(username=username, password=password,
                                   first_name=firstname, last_name=lastname, email=email, is_active=True)
        user.set_password(password)
        profile = Profile.objects.create(user=user)
        user.profile.city = city
        user.profile.address = address
        user.profile.phone = phone
        profile.save()
        group = Group.objects.get(name='Customers')
        group.user_set.add(user)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:home')
        else:
            pass
    return render(request, 'authenticate/signin.html')


def getSessionOrAccountData(request, username):
    try:
        record = account_data.objects.get(username=username)
        request.session[settings.CART_SESSION_ID] = json.loads(record.value)
        return record.value
    except:
        return None


def setSessionOrAccountData(request, key, value):
    if request.user:
        username = request.user
        try:
            record = account_data.objects.get(username=username)
            record.value = value = json.dumps(value)
            record.save()
        except account_data.DoesNotExist:
            record = account_data(username=username,
                                  key=key, value=json.dumps(value))
            record.save()
    else:
        request.session[key] = value
