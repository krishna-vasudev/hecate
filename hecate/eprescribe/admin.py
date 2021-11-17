from django.contrib import admin
from .models import Prescription,Medicine

# Register your models here.
admin.site.register(Prescription)
admin.site.register(Medicine)
