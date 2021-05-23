from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('dj',views.dj),
    path('nj',views.nj),
    path('del1',views.del1),	   
]