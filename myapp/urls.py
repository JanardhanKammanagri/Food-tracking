from django.urls import path
from .import views
urlpatterns=[
    path('',views.index),
    path('loadreg',views.loadReg,name="loadreg"),
    path('loadlogin',views.loadLogin, name="loadlogin"),
    path('register',views.register),
    path('userlogin',views.userlogin),

]