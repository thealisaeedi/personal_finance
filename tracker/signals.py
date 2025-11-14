from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Category
from django.conf import settings


DEFAULT_EXPENSE_CATEGORIES = [
    "Food",
    "Transportation",
    "Entertainment",
    "Bills",
    "Healthcare",
    "Shopping",
]

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        for cat_name in DEFAULT_EXPENSE_CATEGORIES:
            Category.objects.create(name=cat_name, user=instance)
