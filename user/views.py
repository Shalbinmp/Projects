from django.db.models import Q
from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your views here.


def post_user(request):
    obk = ""
    if request.method == 'POST':
        a = request.POST.get('nm')
        b = request.POST.get('em')
        obv = User.objects.filter(Q(name=a) & (Q(email=b) | Q(name=a) | Q(email=b)))
        if len(obv) > 0:
            obk = "user"
        else:
            obj=User()
            obj.name=request.POST.get('nm')
            obj.place=request.POST.get('lo')
            obj.phone=request.POST.get('ph')
            obj.email=request.POST.get('em')
            obj.username=request.POST.get('un')
            obj.password=request.POST.get('ps')
            obj.save()

            ob=Login()
            ob.username=obj.username
            ob.password=obj.password
            ob.u_id=obj.user_id
            ob.type='user'
            ob.save()

    context={
        'x':obk

    }
    return render(request, 'user/post_user.html',context)