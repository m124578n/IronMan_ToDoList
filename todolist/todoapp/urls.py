from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', views.api, name="api"),
    path('api/add/', views.add, name="add"),
    path('api/delete/<int:todo_id>', views.delete, name="delete"),
    path('api/update/<int:todo_id>', views.update, name="update"),
]