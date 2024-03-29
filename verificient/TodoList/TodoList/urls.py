"""TodoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('user_signup/',views.user_signup,name="user_signup"),
    path('u_login/',views.u_login,name="u_login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('new_task/',views.new_task,name="new_task"),
    path('u_logout/',views.u_logout,name="u_logout"),
    path('update/<rid>',views.update,name="update"),
    path('delete/<rid>',views.delete,name="delete"),
]
