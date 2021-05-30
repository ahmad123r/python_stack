from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('cr', views.cr),
    path('suc',views.suc),
    path('logout',views.logout ),
    path('login',views.login),
    path('delete/<int:id>',views.delete),
    path('add_book',views.add_book),
    path('add_fav/<int:id>',views.add_fav),  
    path('book/<int:id>',views.show),
    path('delete1/<int:id>',views.delete1),
    path('update/<int:id>',views.update),
    path('n_fav/<int:id>',views.n_fav),
    
]