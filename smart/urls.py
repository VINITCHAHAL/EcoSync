from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('admined_profile/',views.admined_profile,name='admined_profile'),
    path('map/',views.map,name='map'),
    path('admined/',views.admined,name='admined'),
    path('data/',views.data,name='data'),
    path('details/',views.details,name='details'),
    path('predict/',views.predict,name='predict'),
    

   ]