from django.contrib import admin
from CBVapp.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display =['title','author','pages','price']

admin.site.register(Book,BookAdmin)
