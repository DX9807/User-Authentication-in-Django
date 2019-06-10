from django.urls import path
from .import views

app_name='basic_app'


urlpatterns=[

            #path('',views.index,name='index'),
            path('basic_app/userlogin.html/',views.userlogin,name='userlogin'),
            path('basic_app/register.html/',views.register,name='register'),

]
