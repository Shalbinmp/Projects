from django.shortcuts import render

from auditorium.models import Auditorium
from rating.models import Rating
import datetime
# Create your views here.


def post_rating(request):
    ss=request.session["u_id"]
    obb = Auditorium.objects.all()
    context = {
        'x': obb
    }
    if request.method=='POST':
        obj=Rating()
        obj.rating=request.POST.get('rating')
        obj.date=datetime.datetime.today()
        obj.aud_id=request.POST.get('au')
        obj.user_id=ss
        obj.save()
    return render(request, 'rating/post_rating.html',context)


def view_rating(request):
    obj = Rating.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'rating/view_rating.html',context)

def view_admin(request):
    obj = Rating.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'rating/view_admin.html',context)


def view_user(request):
    obj = Rating.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'rating/view_user.html',context)


