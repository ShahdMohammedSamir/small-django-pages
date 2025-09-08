from django.contrib import admin # type: ignore
from .models import Plant
from .models import Login
# Register your models here.
admin.site.register(Plant)
admin.site.register(Login)