from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class SellingOn(models.Model):
    sotre_location = models.CharField(max_length=200, blank=True, null=True,)
    sotre_intelligence = models.CharField(max_length=200, blank=True, null=True,)
    sotre_links = models.CharField(max_length=200, blank=True, null=True,)
    sotre_ads = models.CharField(max_length=200, blank=True, null=True,)

    class Meta:
        verbose_name_plural = "SellingOn"

    def __str__(self):
        return self.sotre_ads


class Suppliers(models.Model):
    suppliers_location = models.CharField(max_length=200, blank=True, null=True,)
    suppliers_links = models.CharField(max_length=200, blank=True, null=True,)

    class Meta:
        verbose_name_plural = "Suppliers"

    def __str__(self):
        return self.suppliers_links


class Countries(models.Model):
    percentage= models.IntegerField(default=0)
    countries = models.CharField(max_length=200, blank=True, null=True,)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.countries


class Gender(models.Model):
    male = models.IntegerField(default=0)
    female = models.IntegerField(default=0)
    unknown = models.IntegerField(default=0)
   
    class Meta:
        verbose_name_plural = "Gender"

    def __str__(self):
        return self.male


class Product(models.Model):

    class ProductObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, help_text = "This refer to the name of the product")
    kind_ads = models.CharField(max_length=250, blank=True, null=True, help_text = "FaceBook, Instagram, tiktok...")
    media_ads = models.CharField(max_length=250, blank=True, null=True, help_text = "Video, Photo, both")
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='products/default.jpg')
    ads_image = models.ImageField(
        _("Image"), upload_to=upload_to, default='products/default.jpg')
    published = models.DateTimeField(default=timezone.now, help_text = "First time we saw this ads")
    we_found = models.DateTimeField(default=timezone.now, help_text = "This ads wa created between")
    likes = models.IntegerField(default=0, help_text = "Amount of likes generated")
    product_cost = models.IntegerField(default=0, help_text = "Price pay to buy this product")
    selling_price = models.IntegerField(default=0, help_text = "Price you can sell this product")
    profit_margin = models.IntegerField(default=0, help_text = "Profit you get from this product")
    number_of_suppliers= models.IntegerField(default=0,  help_text = "Number of suppliers we get for this product")
    number_of_comment= models.IntegerField(default=0,  help_text = "Number of comment we get for this product")
    number_of_likes= models.IntegerField(default=0,  help_text = "Number of likes we get for this product")
    countries = models.ForeignKey(
        Countries, on_delete=models.PROTECT, blank=True, null=True,)
    selling_on = models.ForeignKey(
        SellingOn, on_delete=models.PROTECT, blank=True, null=True,)
    suppliers = models.ForeignKey(
        Suppliers, on_delete=models.PROTECT, blank=True, null=True,)
    gender = models.ForeignKey(
        Gender, on_delete=models.PROTECT, blank=True, null=True,)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='snooperspy_products') 
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    productobjects = ProductObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


