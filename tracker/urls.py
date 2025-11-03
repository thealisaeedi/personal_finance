from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('list/', views.transaction_list, name='transaction_list'),
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
]