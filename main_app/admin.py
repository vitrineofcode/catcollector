from django.contrib import admin
# add Feeding to the import
from .models import Cat, Feeding, Toy

admin.site.register(Cat)

admin.site.register(Feeding)

admin.site.register(Toy)