from django.contrib import admin

from venues.models import Venue, Category

# Register your models here.
admin.site.register(Venue)
admin.site.register(Category)
