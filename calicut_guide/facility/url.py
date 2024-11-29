from django.conf.urls import url
from facility import views
urlpatterns=[
    url('post_facility/',views.facility),
    url('view_facility/', views.viewfacility),
    url('request_fac/', views.viewfacility_req),
    url('mng/',views.manage),
    url('working/(?P<idd>\w+)', views.working),
    url('closed/(?P<idd>\w+)', views.closed),
    url('public/',views.public_vw)



]