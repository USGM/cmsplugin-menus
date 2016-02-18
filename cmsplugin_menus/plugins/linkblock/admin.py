from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from models import LinkBlock

# Classes with placeholders must register with PlaceholderAdmin
class PlaceholderAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
        pass
admin.site.register(LinkBlock, PlaceholderAdmin)
