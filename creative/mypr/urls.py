from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('campaign', views.campaign, name='campaign'),
    path('pricing', views.pricing, name='pricing'),
    path('forbrands', views.forbrands, name='forbrands'),
]