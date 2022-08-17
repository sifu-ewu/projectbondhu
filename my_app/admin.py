from django.contrib import admin

# Register your models here.
from .models import Project,Tag, doctor,reviews
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(reviews)
admin.site.register(doctor)

