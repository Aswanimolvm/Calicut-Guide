from django.conf.urls import url
from news import views
urlpatterns=[
    url('post_news/',views.news),
    url('view_news/', views.viewnews),
    url('vs/', views.vn),
    url('delete/(?P<idd>\w+)',views.delete)

]