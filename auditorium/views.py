from django.shortcuts import render
from auditorium.models import Auditorium
from django.core.files.storage import FileSystemStorage
# Create your views here.
from login.models import Login
from django.db.models import Q


def post_audi(request):
    obk=""
    if request.method=='POST':
        a=request.POST.get('nm')
        b=request.POST.get('em')
        obv=Auditorium.objects.filter(Q(name=a) & (Q(email=b)  |  Q(name=a) | Q(email=b)))
        if len (obv) > 0:
            obk="user"
        else:
            obj=Auditorium()
            obj.name=request.POST.get('nm')
            obj.phone=request.POST.get('ph')
            obj.email=request.POST.get('em')
            obj.username=request.POST.get('un')
            obj.password=request.POST.get('ps')
            # obj.image=request.POST.get('im')
            myfile=request.FILES['im']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name, myfile)
            obj.image=myfile.name
            obj.status='none'
            obj.location=request.POST.get('lo')
            obj.description=request.POST.get('de')
            obj.save()
    context={
        'x':obk
    }


    return render(request, 'auditorium/post_auditorium.html',context)


def view_audi(request):
    obj=Auditorium.objects.all()
    context={
        'x':obj
    }
    return render(request, 'auditorium/view_auditorium.html',context)


def mng_audi(request):
    obj=Auditorium.objects.filter(status='none')
    context={
        'x':obj
    }
    return render(request, 'auditorium/manage.auditorium.html',context)


def approv_audi(request,idd):
    obj=Auditorium.objects.get(aud_id=idd)
    obj.status='approved'
    obj.save()
    ob = Login()
    ob.username = obj.username
    ob.password = obj.password
    ob.u_id = obj.aud_id
    ob.type = 'auditorium'
    ob.save()
    return mng_audi(request)


def reject_audi(request,idd):
    obj=Auditorium.objects.get(aud_id=idd)
    obj.status='rejected'
    obj.save()
    return mng_audi(request)


def updt_pro(request):
    ss=request.session["u_id"]
    obj = Auditorium.objects.get(aud_id=ss)
    context = {
        'x': obj
    }
    if request.method == 'POST':
        obj = Auditorium.objects.get(aud_id=ss)
        obj.name = request.POST.get('nm')
        obj.phone = request.POST.get('ph')
        obj.email = request.POST.get('em')
        obj.username = request.POST.get('un')
        obj.password = request.POST.get('ps')
        # obj.image = request.POST.get('im')
        myfile = request.FILES['im']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.location = request.POST.get('lo')
        obj.description = request.POST.get('de')
        obj.save()
    return render(request, 'auditorium/update_profile.html',context)
