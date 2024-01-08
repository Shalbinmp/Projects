from django.shortcuts import render
from facilities.models import Facilities
from auditorium.models import Auditorium
from booking.models import Booking
# Create your views here.
from django.db.models import Q


def post_facilities(request):
    ss = request.session["u_id"]
    if request.method=='POST':
        obj=Facilities()
        obj.aud_id=ss
        obj.facilities=request.POST.get('fc')
        obj.amount=request.POST.get('am')
        obj.save()
    return render(request, 'facilities/post_facilities.html')


def view_fac(request):
    if request.method=='POST':
        vv=request.POST.get('lop')
        # kk=request.POST.get('dt')
        obj = Facilities.objects.filter(aud__name__icontains=vv)
        # obj1=Booking.objects.filter(date=kk)
        context = {
            'x': obj,
            # 'y':obj1
        }

        return render(request, 'facilities/view_user.html', context)
    else:
        obj = Facilities.objects.filter(aud__status='approved')
        # obj1=Booking.objects.filter(book_sts='Booked')
        context = {
            'x': obj,
            # 'y':obj1
        }
    return render(request, 'facilities/view_user.html',context)


def mng_fac(request):
    ss=request.session["u_id"]
    obj = Facilities.objects.filter(aud_id=ss)
    context = {
        'x': obj
    }
    return render(request, 'facilities/view_facility.html',context)


def updt_fac(request,idd):
    obj = Facilities.objects.get(fac_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=Facilities.objects.get(fac_id=idd)
        obj.facilities=request.POST.get('fc')
        obj.amount=request.POST.get('am')
        obj.save()
        return mng_fac(request)
    return render(request, 'facilities/update_fac.html', context)


def dlt_fac(request,idd):
    obj=Facilities.objects.get(fac_id=idd)
    obj.delete()
    return mng_fac(request)
