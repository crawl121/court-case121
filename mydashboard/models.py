from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4

# Create your models here.

class ClientRecord(models.Model):
    GENDER_CHOICE = [("male", "Male"), ("female", "Female"), ("other", "Other")]

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=100)
    identity = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    remark = models.CharField(max_length=500, blank=True,)

    agent_fullname = models.CharField(max_length=100, blank=True)
    agent_ph = models.CharField(max_length=50, blank=True)
    agent_identity = models.CharField(max_length=50, blank=True)

    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)



    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name}"
    
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.full_name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.full_name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(ClientRecord, self).save(*args, **kwargs)
