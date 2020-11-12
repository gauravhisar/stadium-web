from django.urls import path

from . import views

urlpatterns =[
    path('signin',views.signin,name='signin'),
    path('verify_user', views.verify_user, name='verify_user'),
    path('records',views.records,name='records'),
    path('signup', views.signup,  name='signup'),
    path('store_user', views.store_user, name='store_user')

]