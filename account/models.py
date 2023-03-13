from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from account import managers as account_managers
# Create your models here.

class TimeStampModel(models.Model):
    id = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractBaseUser,PermissionsMixin,TimeStampModel):
    # TODO: user info field
    email = models.EmailField(max_length = 64, unique = True)
    mobile = models.PositiveBigIntegerField()
    is_email_verified = models.BooleanField(default = False)
    is_mobile_verified = models.BooleanField(default = False)

    # TODO: user permissions field
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile"]

    objects = account_managers.UserManager()

    class Meta:
        db_table = "users"  # Table Name

        


    def __str__(self):
        return self.email

