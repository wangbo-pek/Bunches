from django.urls import path

from bunch01 import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('show/', views.show, name='show')
]