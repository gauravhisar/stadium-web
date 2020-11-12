from django.urls import path

from . import views

urlpatterns =[

    path('', views.signin,  name='signin'),
    path('verify_user', views.verify_user, name='verify_user')
]