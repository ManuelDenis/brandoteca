import uuid
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
import DataChoices.country
from cloudinary.models import CloudinaryField


class Newsletter(models.Model):
    email = models.EmailField(unique=True, default='')

    def __str__(self):
        return str(self.email)


class Categories(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    is_brand_of_the_month = models.BooleanField(default=False)

    name = models.CharField(max_length=64, unique=True)
    motto = models.CharField(max_length=200, null=True, blank=True)
    founding_year = models.IntegerField(choices=DataChoices.country.FOUNDING_YEAR, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)

    entity = models.CharField(max_length=200, null=True, blank=True)
    vat_number = models.CharField(max_length=15, null=True, blank=True)
    reg_no = models.CharField(max_length=30, null=True, blank=True)
    euid = models.CharField(max_length=30, null=True, blank=True)

    website = models.URLField(max_length=200, null=True, blank=True)
    video_url = models.URLField(max_length=200, null=True, blank=True)

    cover = CloudinaryField('cover', null=True, blank=True)
    logo = CloudinaryField('logo', null=True, blank=True)

    facebook = models.URLField(max_length=200, null=True, blank=True)
    youtube = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)

    slug = AutoSlugField(populate_from='name', unique=True, max_length=255)

    type = models.CharField(max_length=20, choices=DataChoices.country.BRAND_TYPES, null=True, blank=True)
    main_category = models.CharField(max_length=105, choices=DataChoices.country.BRAND_CATEGORY, null=True, blank=True)
    categories = models.ManyToManyField(Categories, null=True, blank=True)

    country = models.CharField(max_length=50, choices=DataChoices.country.COUNTRY, null=True, blank=True)
    city = models.CharField(max_length=100, choices=DataChoices.country.ORASE, default='Bucuresti', null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE)
    terms = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
