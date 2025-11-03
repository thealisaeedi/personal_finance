from django.shortcuts import render, redirect
from .models import Transaction, Category
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


def landing(request):
    return render(request, 'tracker/landing.html')

@login_required
def report(request):
    transactions = Transaction.objects.filter(user=request.user)
    total_income = transactions.filter(type='IN').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(type='OUT').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense


    categories = Category.objects.filter(user=request.user)
    category_data = []
    for category in categories:
        income = transactions.filter(type='IN', category=category).aggregate(Sum('amount'))['amount__sum'] or 0
        expense = transactions.filter(type='OUT', category=category).aggregate(Sum('amount'))['amount__sum'] or 0
        category_data.append({
            'name': category.name,
            'income': float(income),
            'expense': float(expense),
        })

    # Filters
    category_id = request.GET.get('category')
    type_filter = request.GET.get('type')
    
    if category_id:
        transactions = transactions.filter(category__id=category_id)
    if type_filter:
        transactions = transactions.filter(type=type_filter)


    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'categories': categories,
        'category_data': category_data,
    }

    return render(request, 'tracker/report.html', context)

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

@login_required
def dashboard(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user).order_by('-date')[:5]
    total_income = Transaction.objects.filter(user=user, type='IN').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Transaction.objects.filter(user=user, type='OUT').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    pie_data = {
        'income': float(total_income),
        'expense': float(total_expense),
    }

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'pie_data': pie_data,
    }

    return render(request, 'tracker/dashboard.html', context)

