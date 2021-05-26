from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new',views.new),
    path('create',views.create),
    path('show/<int:id>',views.show),
    path('delete/<int:id>',views.delete),
    path('<int:id>/edit',views.edit), 
    path('update/<int:id>',views.update),
]