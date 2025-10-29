from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('IN', 'Income'),
        ('OUT', 'Expense'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"