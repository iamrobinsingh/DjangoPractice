from django.contrib import admin
from modelManagerApp.models import Staff,ProxyStaff

# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display=['sno','sname','ssal','saddr']


class ProxyStaffAdmin(admin.ModelAdmin):
    list_display=['sno','sname','ssal','saddr']


admin.site.register(Staff,StaffAdmin)
admin.site.register(ProxyStaff,ProxyStaffAdmin)
