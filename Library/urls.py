from django.urls import path,include

from . import views

urlpatterns = {

   path('insert_Book', views.insert_Book,"insert_Book"),
   path('list_Book', views.list_Book,"list_Book"),
   path('detail_Book', views.detail_Book,"detail_Book"),
   path('update_Book', views.update_Book,"update_Book"),
   path('delete_Book', views.delete_Book,"delete_Book"),
   path('registration', views.registration,"registration"),
   path('login', views.login,"login"),
   path('Home', views.Home,"Home"),
}
