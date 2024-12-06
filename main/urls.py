from django.urls import path
from main.views import AboutView, AboutViewSomeUrl, RequestLogView

urlpatterns = [

    path('', AboutView.as_view(), name='about_us'),
    path('some_url/', AboutViewSomeUrl.as_view(), name='about_us'),
    path('request-logs/', RequestLogView.as_view(), name='request_logs'),

]
