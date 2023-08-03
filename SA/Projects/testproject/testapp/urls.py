from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('form', views.form),
    path('page_not_found', views.error),
    
]
