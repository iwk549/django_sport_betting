from django.db import models

class Subscription(models.Model):
    stripe_id = models.CharField(max_length=255, primary_key=True, unique=True)
    name = models.CharField(max_length=255, unique=True)
