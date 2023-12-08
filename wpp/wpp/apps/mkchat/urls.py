from django.urls import path
from . import views

app_name = 'mkchat'

urlpatterns = [
    path('userPanel/', views.UserPanel.as_view(), name='userPanel'),
    path('userPanel/sendMess', views.SendMess.as_view(), name='sendMess')
]
