from django.urls import path
from . import views

urlpatterns = [
    path('', views.getItem),
    path('<int:pk>', views.getItemById),
    path('add/', views.addItem),
    path('delete/<int:pk>', views.deleteItem),
    path('edit/<int:pk>', views.editItem)
]

