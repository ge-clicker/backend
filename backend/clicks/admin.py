from django.contrib import admin

# Register your models here.
from clicks import models


class ClickRecordAdmin(admin.ModelAdmin):
    pass


class PartyAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.ClickRecord, ClickRecordAdmin)
admin.site.register(models.Party, PartyAdmin)
