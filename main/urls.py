from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('advertisements/', views.advertisements, name="advertisements"),
    path('advertisement/<int:ad_id>/', views.advertisement_detail, name='advertisement_detail'),
    path('create_advertisement/', views.create_advertisement, name="create_ad"),
    path('contacts/', views.contacts, name="contacts"),
]
