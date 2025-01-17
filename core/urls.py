"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('testowo', views.TestView.as_view(), name='testowo'),
    path('get_institutions/', views.get_institutions, name='get_institutions'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('add_donation', views.AddDonationView.as_view(), name='add_donation'),
    path('profil/', views.UserPersonalView.as_view(), name='profil'),

]
