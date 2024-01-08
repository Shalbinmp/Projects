from django.conf.urls import url
from complaint import views
urlpatterns = [
    url('post_com/', views.post_complaint),
    url('post_rply/(?P<idd>\w+)', views.post_reply),
    url('vie_comp/', views.view_complaint),
    url('view_com_rp/', views.view_comp_rply),
    url('view_rp/', views.view_reply),
]