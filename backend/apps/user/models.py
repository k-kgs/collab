from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name="Email Address", unique=True)
    # phone_number = models.CharField(
    #     _("Phone number"), null=True, max_length=15, db_index= True
    # )
    def __str__(self):
        return self.username