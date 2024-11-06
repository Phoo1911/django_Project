from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


transaction_list = []

def transactions_page(request):
    return render(request, 'transactions/transactions.html', {'transactions': transaction_list})


@csrf_exempt  # Allow POST requests without CSRF verification for simplicity
def add_transaction(request):
    if request.method == 'POST':
        transaction_description = request.POST.get('transaction_description')
        transaction_amount = request.POST.get('transaction_amount')
        transaction_type = request.POST.get('transaction_type')

        # Create a transaction dictionary and append it to the list
        transaction = {
            'description': transaction_description,
            'amount': transaction_amount,
            'type': transaction_type,
        }
        transaction_list.append(transaction)  # Add to the list
        return redirect('transactions_page')  # Redirect to the transactions page
    return HttpResponse("Method not allowed", status=405)


def delete_transaction(request, transaction_index):
    if 0 <= transaction_index < len(transaction_list):
        transaction_list.pop(transaction_index)  # Remove the transaction by index
    return redirect('transactions_page')  # Redirect to the transactions page


