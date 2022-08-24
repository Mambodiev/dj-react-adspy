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

class ProductInsightsRating(models.Model):
    text = models.CharField(max_length=200, blank=True)
    Product_Breakthrough_rating = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "ProductInsightsRating"

    def __str__(self):
        return self.text


class OrdersStatistics(models.Model):
    Total_last_6_months = models.IntegerField(default=0)
    Total_last_30_days = models.IntegerField(default=0)
    Total_last_14_days = models.IntegerField(default=0)
    Total_last_7_days = models.IntegerField(default=0)
    daily_approximation = models.IntegerField(default=0)
   
    class Meta:
        verbose_name_plural = "OrdersStatistics"

    def __str__(self):
        return self.daily_approximation


class ProductInsights(models.Model):
    text = models.CharField(max_length=200, blank=True)
    Product_Breakthrough = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "ProductInsights"

    def __str__(self):
        return self.text


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


class CompetitorMeter(models.Model):
    percentage = models.IntegerField(default=0)
    competiton = models.CharField(max_length=200, blank=True, null=True,)

    class Meta:
        verbose_name_plural = "CompetitorMeters"

    def __str__(self):
        return self.competiton


class TopCustomerCountries(models.Model):
    percentage = models.IntegerField(default=0)
    competiton = models.CharField(max_length=200, blank=True, null=True,)

    class Meta:
        verbose_name_plural = "TopCustomerCountries"

    def __str__(self):
        return self.competiton


class FacebookTargetArea(models.Model):
    Business_Industry = models.CharField(max_length=200, blank=True, null=True,)
    Entertainment = models.CharField(max_length=200, blank=True, null=True,)
    Family_relationships = models.CharField(max_length=200, blank=True, null=True,)
    Fitness_wellness = models.CharField(max_length=200, blank=True, null=True,)
    Food_drink = models.CharField(max_length=200, blank=True, null=True,)
    Hobbies_activities = models.CharField(max_length=200, blank=True, null=True,)
    Shopping_fashion = models.CharField(max_length=200, blank=True, null=True,)
    Sports_outdoors = models.CharField(max_length=200, blank=True, null=True,)
    Technology = models.CharField(max_length=200, blank=True, null=True,)
   
    class Meta:
        verbose_name_plural = "FacebookTargetArea"

    def __str__(self):
        return self.Technology
class Product(models.Model):

    class ProductObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='products/default.jpg')
    published = models.DateTimeField(default=timezone.now)
    we_found = models.DateTimeField(default=timezone.now)
    orders = models.IntegerField(default=0)
    product_cost = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    profit_margin = models.IntegerField(default=0)
    total_sales = models.IntegerField(default=0)
    number_of_suppliers= models.IntegerField(default=0)
    number_of_store_selling= models.IntegerField(default=0)
    product_insights_rating = models.ForeignKey(
        ProductInsightsRating, on_delete=models.PROTECT, blank=True, null=True,)
    orders_statistics = models.ForeignKey(
        OrdersStatistics, on_delete=models.PROTECT, blank=True, null=True,)
    product_insights = models.ForeignKey(
        ProductInsights, on_delete=models.PROTECT, blank=True, null=True,)
    competitor_meter = models.ForeignKey(
        CompetitorMeter, on_delete=models.PROTECT, blank=True, null=True,)
    top_customer_countries = models.ForeignKey(
        TopCustomerCountries, on_delete=models.PROTECT, blank=True, null=True,)
    selling_on = models.ForeignKey(
        SellingOn, on_delete=models.PROTECT, blank=True, null=True,)
    suppliers = models.ForeignKey(
        Suppliers, on_delete=models.PROTECT, blank=True, null=True,)
    facebook_target_area = models.ForeignKey(
        FacebookTargetArea, on_delete=models.PROTECT, blank=True, null=True,)
    view_facebook_ads = models.CharField(max_length=250, blank=True, null=True,)
    view_on_amazon = models.CharField(max_length=250, blank=True, null=True,)
    view_on_youtube = models.CharField(max_length=250, blank=True, null=True,)
    view_tiktok_ads = models.CharField(max_length=250, blank=True, null=True,)
    view_pinterest_ads = models.CharField(max_length=250, blank=True, null=True,)

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


