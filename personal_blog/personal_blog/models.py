from django.db import models
from django.contrib.auth.models import User, Group


class NewUser(models.Model):
    user = models.ForeignKey(User)
    phone_number = models.CharField(max_length=16, null=True)
    address = models.CharField(max_length=100, blank="")
    signed_form = models.NullBooleanField(blank=False, null=True)
    approved = models.NullBooleanField(blank=False, null=True)
    street_address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    vol_before = models.BooleanField(default=False)
    contact = models.BooleanField(default=False)
    comments = models.CharField(max_length=10240, null=True)
