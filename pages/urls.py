from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name = 'index'),
	path('project-overview/', views.projectOverview, name="project-overview"),
    #path('projects/<int:category>/', views.projects, name = 'category_projects'),
    #path('categorey/', views.categorey, name = 'categorey'),
	path('projects/', views.projects, name = 'projects'),

]