from django.urls import path
from .import views
app_name = 'shop'


urlpatterns = [
    path('', views.index, name='listproduct'),
    path('insertCart/<int:id>/', views.insertCart, name = 'insertCart'),
]