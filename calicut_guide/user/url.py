from django.conf.urls import url
from user import views
urlpatterns=[
    url('register/',views.post_user),
    # url('view_registration/', views.view_registration),
    # url('accepted/(?P<idd>\w+)', views.accept),
    # url('rejected/(?P<idd>\w+)', views.reject)

]


