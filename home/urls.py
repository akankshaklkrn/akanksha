from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name='home'
urlpatterns = [
    path('',views.index,name='index'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('add_gifts',views.add_gifts,name='add_gifts'),
    path('select_gift', views.select_gift,name='select_gift'),
    path('form',views.form,name='form'),
    path('view_selected_gifts',views.view_selected_gifts,name='vs'),
    path('final',views.final,name='final')
]