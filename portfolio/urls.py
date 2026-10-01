from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('api/info/', views.api_info, name='api_info'),
    path('api/contact/', views.api_contact, name='api_contact'),
    path('api/verify-doc/', views.api_verify_doc, name='api_verify_doc'),
    path('api/match-resume/', views.api_match_resume, name='api_match_resume'),
]
