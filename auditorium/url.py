from django.conf.urls import url
from auditorium import views

urlpatterns=[
    url('add_aud/', views.post_audi),
    url('view_aud/', views.view_audi),
    url('mng_aud/', views.mng_audi),
    url('aprv/(?P<idd>\w+)', views.approv_audi),
    url('rejet/(?P<idd>\w+)', views.reject_audi),
    url('updt/', views.updt_pro),
]