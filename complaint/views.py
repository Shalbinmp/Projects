from django.shortcuts import render
from complaint.models import Complaint
import datetime
from auditorium.models import Auditorium
# Create your views here


def post_complaint(request):
    ss = request.session["u_id"]
    obb=Auditorium.objects.all()
    context={
        'n':obb
    }

    if request.method=='POST':
        obj=Complaint()
        obj.complaint=request.POST.get('comp')
        obj.reply='pending'
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.user_id=ss
        obj.aud_id=request.POST.get('nn')
        obj.save()
    return render(request, 'complaint/post_comp.html',context)


def post_reply(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(comp_id=idd)
        obj.reply=request.POST.get('rp')
        obj.save()
        return view_complaint(request)
    return render(request, 'complaint/post_reply.html')


def view_complaint(request):
    obj = Complaint.objects.filter(reply='pending')
    context = {
        'x': obj
    }
    return render(request, 'complaint/view_comp.html',context)


def view_comp_rply(request):
    ss=request.session["u_id"]
    obj = Complaint.objects.filter(aud_id=ss)
    context = {
        'x': obj
    }
    return render(request, 'complaint/view_complaint_reply.html',context)


def view_reply(request):
    ss=request.session["u_id"]
    obj = Complaint.objects.filter(user_id=ss)
    context = {
        'x': obj
    }
    return render(request, 'complaint/view_rply.html',context)
