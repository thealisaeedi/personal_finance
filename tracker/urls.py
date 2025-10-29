from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_transaction, name='add_transaction'),
    path('list/', views.transaction_list, name='transaction_list'),
    path('report/', views.report, name='report'),
]