from django.contrib import admin
from location.models import Link, Tag


class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', )
    list_filter = ('tags', 'created_at', 'updated_at')
    search_fields = ('name', 'link')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ('Link', {
            'fields': ('name', 'link')
        }),
        ('Tags', {
            'fields': ('tags', )
        }),
        ('Change History', {
            'classes': ('collapse', ),
            'fields': ('created_at', 'updated_at')
        })
    ]

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'column' )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'position', 'column' )
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ('Link', {
            'fields': ('name', 'position', 'column' )
        }),
        ('Change History', {
            'classes': ('collapse', ),
            'fields': ('created_at', 'updated_at')
        })
    ]

admin.site.register(Link, LinkAdmin)
admin.site.register(Tag, TagAdmin)
