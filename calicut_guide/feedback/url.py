from django.conf.urls import url
from feedback import views
urlpatterns=[
url('post_feedback/',views.feedback),
    url('view_feedback/', views.viewfeedback)

]