from django.contrib import admin # type: ignore
from .models import books

# Register your models here.
admin.site.register(books)
