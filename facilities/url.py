from django.conf.urls import url
from facilities import views
urlpatterns = [
    url('add_facility/', views.post_facilities),
    url('view_us/', views.view_fac),
    url('mng_fac/', views.mng_fac),
    url('upd_fac/(?P<idd>\w+)', views.updt_fac),
    url('dlt_fac/(?P<idd>\w+)', views.dlt_fac),
]