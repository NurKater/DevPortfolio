from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='projects', permanent=False)),
    path('projects/', views.projects_list, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('blogs/', views.blog_ls, name='blogs'),
]
