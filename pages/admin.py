from pages.models import Team
from django.contrib import admin
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10px" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name',
                    'designation', 'created_date')
    list_display_links = ('id', 'first_name', 'thumbnail')
    search_fields = ('first_name', 'last_name', 'designati on')


admin.site.register(Team, TeamAdmin)
