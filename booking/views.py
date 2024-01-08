from django.shortcuts import render
from django.db.models import Q

from booking.models import Booking
# Create your views here.


def post_book(request,idd,idd1):
    obk=""
    ss=request.session["u_id"]
    if request.method=='POST':
        a = request.POST.get('dt')
        b = request.POST.get('ti')
        obv = Booking.objects.filter(Q(date=a) & (Q(time=b) | Q(date=a) | Q(time=b)))
        if len(obv) > 0:
            obk = "Date exist"
        else:
            obj=Booking()
            obj.time=request.POST.get('ti')
            obj.date=request.POST.get('dt')
            obj.fac_id=idd
            obj.user_id=ss
            obj.aud_id=idd1
            obj.reminders=request.POST.get('rem')
            obj.status='pending'
            obj.book_sts='Pending'
            obj.save()
            obk = "Succefully Booked"
    context = {
        'msg': obk
        }
    return render(request, 'booking/booking_sts.html',context)


def mng_book(request):
    ss=request.session["u_id"]
    obj=Booking.objects.filter(aud_id=ss, status='pending')
    context={
        'x':obj
    }
    return render(request, 'booking/mng_booking.html',context)


def approv_book(request,idd):
    obj=Booking.objects.get(book_id=idd)
    obj.status='approved'
    obj.save()
    return mng_book(request)


def reject_book(request,idd):
    obj=Booking.objects.get(book_id=idd)
    obj.status='rejected'
    obj.save()
    return mng_book(request)


def book_sts(request):
    ss = request.session["u_id"]
    obj=Booking.objects.filter(status='approved', user_id=ss)
    context={
        'x':obj
    }
    return render(request, 'booking/boooking_sts.html',context)


def view_user(request):
    if request.method == 'POST':
        vv=request.POST.get('lop')

        obj = Booking.objects.filter(aud__name__icontains=vv)
        context = {
            'x': obj,
                # 'y':obj1
        }

        return render(request, 'booking/view_user.html', context)
    else:
        obj=Booking.objects.all()
        context={
            'x':obj
        }
    return render(request, 'booking/view_user.html',context)
