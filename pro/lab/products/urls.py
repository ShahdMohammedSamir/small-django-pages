from django.urls import path # type: ignore
from .views import product,products

urlpatterns = [
    path('',products , name='products'),
    path('<int:pk>/',product, name='product'),
    ]