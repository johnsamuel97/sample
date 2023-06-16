from django.contrib import admin

# Register your models here.
from website.models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display=['name','mobile_no','email','address']
admin.site.register(Record,RecordAdmin)