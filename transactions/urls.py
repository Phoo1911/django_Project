# transactions/urls.py
from django.urls import path
from .views import transactions_page, add_transaction, delete_transaction

urlpatterns = [
    path('', transactions_page, name='transactions_page'),  # Main transactions page
    path('add/', add_transaction, name='add_transaction'),  # Add transaction
    path('delete/<int:transaction_index>/', delete_transaction, name='delete_transaction'),  # Delete transaction
]










