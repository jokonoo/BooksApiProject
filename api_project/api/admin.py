from django.contrib import admin
from .models import Books, Categories, Authors

admin.site.register(Books)
admin.site.register(Categories)
admin.site.register(Authors)

# Register your models here.
