from django.contrib import admin

# Register your models here.
from scraping.models import YarnProduct, WebResource

admin.site.register(YarnProduct)
admin.site.register(WebResource)
