from django.urls import path
from .views import homePageView  # Importamos la vista que creaste

urlpatterns = [
    path('', homePageView, name='home'),  # URL vacía = página principal
]
