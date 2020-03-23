from django.contrib import admin
from inventory.models import Inventory, Item

# Register your models here
admin.site.register(Inventory)
admin.site.register(Item)