from django.conf.urls import url
from complaint import views
urlpatterns=[
    url('post_complaint/',views.complaint),
    # url('replay/(?P<idd>\w+)', views.post_replay),
    url('view_complaint/', views.viewcomplaint),
    # url('view_replay/', views.view_replay)

]