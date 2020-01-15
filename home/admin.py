from django.contrib import admin
from .models import Gift,user
# Register your models here.
admin.site.register(Gift)
admin.site.register(user)
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)