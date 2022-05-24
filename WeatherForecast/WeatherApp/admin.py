from django.contrib import admin
from .models import City

# Импортируем таблицу из файла: models.py
admin.site.register(City)

