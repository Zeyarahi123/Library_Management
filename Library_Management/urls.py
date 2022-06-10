"""Library_Management URL Configuration

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
from django.urls import path,include

from Library.views import Home,insert_Book,delete_Book,detail_Book,list_Book,login,registration,update_Book

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include("Library.urls")),
    path("Home",Home),
    path("insert_Book",insert_Book),
    path("login", login),
    path("registration",registration),
    path("list_Book",list_Book),
    path("delete_Book",delete_Book),
    path("update_Book",update_Book),
    path("detail_book",detail_Book),

    #path('Library/',include("accounts/views.Home")),
]
