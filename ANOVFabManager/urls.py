"""ANOVFabManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ovfabmanager.urls')),
]

handler500 = 'ovfabmanager.views.error_500'
handler410 = 'ovfabmanager.views.error_410'
handler408 = 'ovfabmanager.views.error_408'
handler404 = 'ovfabmanager.views.error_404'
handler403 = 'ovfabmanager.views.error_403'
handler401 = 'ovfabmanager.views.error_401'
handler400 = 'ovfabmanager.views.error_400'
