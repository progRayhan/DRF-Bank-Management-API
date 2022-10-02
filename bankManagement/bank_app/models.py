from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Please provide an email address")

        email = self.normalize_email(email)

        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

        

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


BANK_CHOICES = (
    ('sonali', "Sonali"),
    ('rupali', "Rupali"),
    ('bangladesh', "Bangladesh"),
    ('world', "World"),
    ('ific', "IFIC"),
)

ACCOUNT_TYPES = (
    ('current', "Current"),
    ('savings', "Savings"),
    ('deposit', "Deposit"),
    ('fixed', "Fixed"),
)

class Bank(models.Model):
    email = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bank_is')
    bank_name = models.CharField(max_length=10, choices=BANK_CHOICES, default='sonali')
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES, default='current')
    balance = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.bank_name} - {self.account_type} - {self.balance}'