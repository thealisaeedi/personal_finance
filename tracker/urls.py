from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('list/', views.transaction_list, name='transaction_list'),
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('category/add', views.add_category, name='add_category'),
    path('transaction/<int:pk>/edit/', views.edit_transaction, name='edit_transaction'),
    path('transaction/<int:pk>/delete/', views.delete_transaction, name='delete_transaction'),
    path('categories/', views.category_manager, name='category_manager'),
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
]