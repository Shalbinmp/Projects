from django.shortcuts import render

# Create your views here.
from facilities.models import Facilities


def home(request):
    return render(request, 'temp/home.html')


def main_home(request):
    return render(request, 'temp/mainhome.html')


def admin(request):
    return render(request, 'temp/admin.html')


def main_admin(request):
    return render(request, 'temp/mainadmin.html')


def user(request):
    return render(request, 'temp/user.html')


def main_user(request):
    return render(request, 'temp/mainuser.html')


def auditorium(request):
    return render(request, 'temp/auditorium.html')


def main_auditorium(request):
    return render(request, 'temp/mainauditorium.html')






