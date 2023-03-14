import datetime
import uuid
from django.contrib.auth.models import User
from django.db import models
from djrichtextfield.models import RichTextField
from autoslug import AutoSlugField
import DataChoices.country
from bt import settings


class Newsletter(models.Model):
    email = models.EmailField(unique=True, default='')

    def __str__(self):
        return str(self.email)


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    is_verified = models.BooleanField(default=False)
    name = models.CharField(max_length=64)
    motto = models.CharField(max_length=200, null=True, blank=True)
    founding_year = models.IntegerField(choices=settings.FOUNDING_YEAR)
    description = RichTextField()
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    entity = models.CharField(max_length=200, default='N/A')
    vat_number = models.CharField(max_length=15, default='N/A')
    reg_no = models.CharField(max_length=30, default='N/A')
    euid = models.CharField(max_length=30, default='N/A')

    website = models.URLField(max_length=200, null=True, blank=True)
    video_url = models.URLField(max_length=200, null=True, blank=True)

    facebook = models.URLField(max_length=200, null=True, blank=True)
    youtube = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)

    slug = AutoSlugField(populate_from='name', unique=True, max_length=255)

    type = models.CharField(max_length=20, choices=settings.BRAND_TYPES)
    main_category = models.CharField(max_length=105, choices=DataChoices.country.BRAND_CATEGORY)
    categories = models.CharField(max_length=105, choices=DataChoices.country.BRAND_CATEGORY, null=True, blank=True)

    country = models.CharField(max_length=50, choices=DataChoices.country.COUNTRY)
    city = models.CharField(max_length=100, choices=DataChoices.country.CITY)

    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE)

    def __str__(self):
        return self.name






