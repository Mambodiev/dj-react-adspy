from django.contrib import admin
from . import models


@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Category)
admin.site.register(models.ProductInsightsRating)
admin.site.register(models.ProductInsights)
admin.site.register(models.OrdersStatistics)
admin.site.register(models.CompetitorMeter)
admin.site.register(models.TopCustomerCountries)
admin.site.register(models.SellingOn)
admin.site.register(models.Suppliers)
admin.site.register(models.FacebookTargetArea)
