from django.conf.urls import url
from user import views
urlpatterns = [
    url('add_usr/', views.post_user),
]