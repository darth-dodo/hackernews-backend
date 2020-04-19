# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class HNUser(TimeStampedModel):
    django_user = models.OneToOneField(
        to=User, primary_key=True, related_name="hn_user", on_delete=models.PROTECT
    )
    bio = models.TextField(null=True, blank=True)

    @property
    def username(self):
        return f"{self.django_user.username}"

    @property
    def first_name(self):
        return f"{self.django_user.first_name}"

    @property
    def last_name(self):
        return f"{self.django_user.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.django_user.email}"

    @property
    def active(self):
        return f"{self.django_user.is_active}"

    @property
    def superuser_access(self):
        return self.django_user.is_superuser

    def __str__(self):
        return f"{self.username}"
