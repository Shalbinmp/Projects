from django.shortcuts import render
from payment.models import Payment
from facilities.models import Facilities
from booking.models import Booking
# Create your views here.


def post_payment(request,idd):
    ss= request.session["u_id"]
    obb=Booking.objects.get(book_id=idd)
    context={
        'v':obb
    }
    if request.method=='POST':
        obj=Payment()
        obj.user_id=ss
        obj.fac_id=1
        obj.cvv=request.POST.get('v')
        obj.card_holder=request.POST.get('n')
        obj.pay_sts='paid'
        obj.book_id=idd
        obj.save()
    return render(request, 'payment/post_payment.html',context)


def view_payment(request):
    ss=request.session["u_id"]
    obj = Payment.objects.filter(book__aud__aud_id=ss)
    context = {
        'x': obj
    }
    return render(request, 'payment/view_payment.html',context)
