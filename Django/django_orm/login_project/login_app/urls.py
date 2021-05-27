from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('cr', views.cr),
    path('suc/<int:id>',views.suc),
    path('logout',views.logout ),
    path('login',views.login),
    path('delete/<int:id>',views.delete),   
    
]