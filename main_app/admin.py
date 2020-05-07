from django.contrib import admin

from . models import Bat, Feeding, Toy

# Register your models here.

admin.site.register(Bat)
admin.site.register(Feeding)
admin.site.register(Toy)