from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('services/', views.services, name='services'),

    path(
        'services/<slug:slug>/',
        views.service_detail,
        name='service_detail'
    ),

    path('portfolio/', views.portfolio, name='portfolio'),

    path(
        'portfolio/<int:project_id>/',
        views.project_detail,
        name='project_detail'
    ),

    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]

