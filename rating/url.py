from django.conf.urls import url
from rating import views
urlpatterns = [
    url('post_rat/', views.post_rating),
    url('view_rat/', views.view_rating),
    url('view_adm/', views.view_admin),
    url('view_userr/', views.view_user),

]