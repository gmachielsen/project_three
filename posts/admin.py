from django.contrib import admin
from .models import Animal, AnimalImages

class ProductImageInline(admin.TabularInline):
    model = AnimalImages
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]
    # prepopulated_fields = {'slug': ('latinName',)}
# class SlugAdmin(admin.ModelAdmin):


admin.site.register(Animal, ProductAdmin)
# Register your models here.
