from django.conf.urls import url
from temp import views
urlpatterns=[
    url('admin/',views.admin),
    url('home/',views.home),
    url('user/',views.user),
    url('org/',views.org),
    url('mhome/',views.mhome),
    url('public/',views.public)
]