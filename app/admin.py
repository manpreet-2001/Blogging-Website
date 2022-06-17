from django.contrib import admin

# Register your models here.
from .models import contact,blog,category,BlogComment

admin.site.register(blog)

admin.site.register(contact)

admin.site.register(category)

admin.site.register(BlogComment)


