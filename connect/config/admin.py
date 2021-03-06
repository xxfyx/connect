from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin

from connect.config.models import SiteConfig


class SiteConfigInline(admin.StackedInline):
    model = SiteConfig
    can_delete = False


class CustomSiteAdmin(SiteAdmin):
    inlines = (SiteConfigInline,)


# Re-register SiteAdmin
admin.site.unregister(Site)
admin.site.register(Site, CustomSiteAdmin)

admin.site.unregister(Group)
