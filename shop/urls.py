from django.urls import path
from .import views
app_name = 'shop'


urlpatterns = [
    path('', views.index, name='listproduct'),
    path('insertCart/<int:id>/', views.insertCart, name = 'insertCart'),
    path('viewCart/', views.viewCart, name = 'viewCart'),
    path('updateCart/<int:id>', views.updateCart, name="updateCart"),
    path('deleteCart/<int:id>', views.deleteCart, name="deleteCart")
]