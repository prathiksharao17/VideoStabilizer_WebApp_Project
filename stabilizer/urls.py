from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('upload/', views.upload_view, name='upload'),
    path('processing/', views.processing_page, name='processing'),
    path('api/stabilize/', views.stabilize_api, name='stabilize_api'),
    path('result/', views.result_view, name='result'),
]