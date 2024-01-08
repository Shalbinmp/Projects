from django.conf.urls import url
from payment import views
urlpatterns = [
    url('addd_pay/(?P<idd>\w+)', views.post_payment),
    url('view_pay/', views.view_payment),
]
