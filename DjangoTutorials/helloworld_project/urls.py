from django.contrib import admin
from django.urls import path, include  # Agrega include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Conecta con urls de la app 'pages'
]
