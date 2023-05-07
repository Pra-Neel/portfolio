"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from custom_auth import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include #includes ley sabai apps ko urls lai link garcha

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('custom_auth.urls')) #yesma apps ko url pattern add gareko
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #to access static files where css and js images are kept
