from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('set-setpoint/', views.form_response),
    path('set-intensity/', views.set_intensity),
    path('success/', views.success)
]