from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('getResource/', views.getResource, name='resource'),
  path('getMeeting/', views.getMeeting, name='meeting'),
  path('getMeetingDetails/<int:id>', views.getMeetingDetails, name='meetingdetails'),
  path('FormMeeting/', views.FormMeeting, name='meetingform'),
  path('FormResource/', views.FormResource, name='resourceform'),
  path('loginmessage/', views.loginmessage, name='loginmessage'),
  path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]


