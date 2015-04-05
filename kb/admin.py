from django.contrib import admin

# Register your models here.
from kb.models import Record,Tag,Tag_Rec

admin.site.register(Record)
admin.site.register(Tag_Rec)
admin.site.register(Tag)