from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('projects/', views.projects_list, name='projects'),
    path('create/', views.create_project, name='create_project'),
    path('profile/', views.profile, name='profile'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'), 
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
]
