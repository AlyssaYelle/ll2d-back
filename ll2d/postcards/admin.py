from django.contrib import admin

# Register your models here.
from .models import Postcard

# Define the admin class
class PostcardAdmin(admin.ModelAdmin):
    list_display = ('dog_img_url', 'author', 'letter', 'approved')
    list_filter = ('approved',)

# Register the admin class with the associated model
admin.site.register(Postcard, PostcardAdmin)

#admin.site.register(Postcard)
