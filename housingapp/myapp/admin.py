from django.contrib import admin

# Register your models here.
from .models import Property, Review
from .models import University

admin.site.register(Property)
admin.site.register(University)
admin.site.register(Review)
