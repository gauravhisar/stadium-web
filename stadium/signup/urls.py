from django.urls import path

from . import views

urlpatterns =[

    path('', views.signup,  name='signup'),
    path('store_user', views.store_user, name='store_user')
]