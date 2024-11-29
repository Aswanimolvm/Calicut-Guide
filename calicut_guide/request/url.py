from django.conf.urls import url
from request import views
urlpatterns=[
url('post_request/(?P<idd>\w+)',views.request),
    url('view_request/', views.view_request),
url('accp/(?P<idd>\w+)',views.accept),

]