from django.conf.urls import url
from temp import views


urlpatterns = [
    url('home/',views.home),
    url('mh/', views.main_home),
    url('admin/',views.admin),
    url('mainadmin/', views.main_admin),
    url('user/',views.user),
    url('mainuser/', views.main_user),
    url('auditorium/',views.auditorium),
    url('mainauditorium/', views.main_auditorium),

]