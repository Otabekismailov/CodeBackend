from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    related_name = 'user'

    def __str__(self):
        return self.username


class VerificationCode(models.Model):
    # class VerificationTypes(models.TextChoices):
    #     REGISTER = "register"
    #     LOGIN = "login"
    #     RECOVER_PASSWORD = "recover_password"

    code = models.CharField(max_length=6)
    user = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="verification_codes", null=True, blank=True
    )
    email = models.EmailField(unique=True, null=True)
    # verification_type = models.CharField(max_length=50, choices=VerificationTypes.choices)
    last_sent_time = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    expired_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.email

    @property
    def is_expire(self):
        return self.expired_at < self.last_sent_time + timedelta(seconds=30)
