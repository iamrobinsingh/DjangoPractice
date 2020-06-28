from django.contrib import admin
from testApplication.models import ContactInfos,Student1,Teacher1,Parent,Child,SubChild

# Register your models here.

admin.site.register(ContactInfos)
admin.site.register(Student1)
admin.site.register(Teacher1)


admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(SubChild)
