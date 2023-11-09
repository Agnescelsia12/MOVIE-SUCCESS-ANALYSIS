
from django.contrib import admin
from django.urls import path
from appdata.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_login),
    path('metta_add/', metta_add),
    path('loadvideo/<int:id>', loadvideo),
    path('metta_display/', metta_display),
    path('collection/', collection),
    path('movie_review/', movie_review),
    path('movie_status/<int:id>', movie_status),
    path('collection/', collection),
    path('meta_update/<int:id>', meta_update),
    path('meta_delete/<int:id>', meta_delete),
    path('meta_edit/<int:id>', meta_edit),
    
]
