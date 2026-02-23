"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/',views.landing,name='landing'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('userdashboard/',views.userdashboard,name='userdashboard'),
    path('logout/',views.logout,name='logout'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),

    path('login1/',views.login1,name='login1'),

    path('admindashboard/add_dept/',views.add_dept,name='add_dept'),
    path('admindashboard/show_dept/',views.show_dept,name='show_dept'),
    path('admindashboard/save_dept/',views.save_dept,name='save_dept'),
    path('admindashboard/add_emp/',views.add_emp,name='add_emp'),
    path('admindashboard/show_emp/',views.show_emp,name='show_emp'),
    path('admindashboard/save_emp/',views.save_emp,name='save_emp'),
    path('',views.empdashboard,name='empdashboard'),
    
]