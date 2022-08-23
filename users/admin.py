from django.contrib import admin

from users.models import City, Country, Person

# Register your models here.
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Person)