from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='shophome'),
    path('contact', views.contactview,name='shophome'),
    path('product/<int:myid>', views.productview,name='productview'),
    path('traker', views.traker,name='shophome'),
    path('about', views.about,name='shophome'),


]
