from django.contrib import admin
from FilterApplication.models import FilterModel

# Register your models here.
class FilterModelAdmin(admin.ModelAdmin):
    list_display =['name','subject','department','date']
admin.site.register(FilterModel,FilterModelAdmin)
