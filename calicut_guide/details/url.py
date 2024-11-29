from django.conf.urls import url
from details import views


urlpatterns=[
    url('post_details/(?P<idd>\w+)',views.details),
    url('view_details/',views.view_details),
    url('view_details_org/',views.view_detail_org),


]
