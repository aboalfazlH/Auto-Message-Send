from django.db import models
from django_full_kit.django_full_kit.models import AdvancedBaseUser,PhoneNumberField,_


class CustomUser(AdvancedBaseUser):
    phone_number = PhoneNumberField(
    verbose_name="شماره تلفن",
    unique=True,
    blank=False,
    null=False,
    )
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ("email","username")