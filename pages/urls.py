from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name = 'index'),
	path('details/<slug:slug>/', views.details, name="details"),
    #path('projects/<int:category>/', views.projects, name = 'category_projects'),
    path('contact', views.contact, name='contact'),
	path('projects/', views.projects, name = 'projects'),
	path('testimonial/', views.testimonial, name = 'testimonial'),
	path('services/', views.services, name = 'services'),
]
