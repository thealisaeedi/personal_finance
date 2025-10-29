from django.shortcuts import render, redirect
from .models import Transaction, Category
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, user=request.user)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(user=request.user)
    return render(request, 'tracker/add_transaction.html', {'form': form})

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'tracker/transaction_list.html', {'transactions': transactions})

