from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('details/<int:pk>', views.detail_record, name = "details"),
    path('delete/<int:pk>', views.delete_record, name = "delete"),
    path('add_post', views.add_post, name = "addpost"),
    path('update_record/<int:pk>', views.update_record, name = "update"),
    
]
