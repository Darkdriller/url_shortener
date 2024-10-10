"""
URL configuration for url_shortener project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# urls.py
from django.urls import path
from shortener import views

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    path('login/', views.login_page, name='login_page'),    # Login page
    path('register/', views.register_page, name='register'),
    path('<str:short_url>/', views.redirect_url, name='redirect_url'),
]

