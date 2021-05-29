from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('author',views.author),
    path('add_author', views.add_author),
    path('books/<int:id>',views.dis),
    path('a_b/<int:id>',views.a_b),
    path('authors/<int:id>',views.dis1),
    path('ps/<int:id>',views.ps)



    	   
]