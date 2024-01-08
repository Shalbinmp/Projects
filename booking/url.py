from django.conf.urls import url
from booking import views
urlpatterns = [
    url('post_book/(?P<idd>\w+)/(?P<idd1>\w+)', views.post_book),
    url('mng_book/', views.mng_book),
    url('aprv_buk/(?P<idd>\w+)', views.approv_book),
    url('rejct_buk/(?P<idd>\w+)', views.reject_book),
    url('book_sts/',views.book_sts),
    url('view_usbook/', views.view_user)
]