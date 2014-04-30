from django.contrib import admin
from bookmarks.models import Link, Tag, Page


class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'colour')
    list_filter = ('tags', 'created_at', 'updated_at')
    search_fields = ('name', 'link', 'colour')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ('Link', {
            'fields': ('name', 'link', 'colour')
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
    list_display = ('name', 'position', 'column', 'colour', 'page')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'position', 'column', 'colour', 'page')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ('Link', {
            'fields': ('name', 'position', 'column', 'colour', 'page')
        }),
        ('Change History', {
            'classes': ('collapse', ),
            'fields': ('created_at', 'updated_at')
        })
    ]


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'position')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ('Link', {
            'fields': ('name', 'position')
        }),
        ('Change History', {
            'classes': ('collapse', ),
            'fields': ('created_at', 'updated_at')
        })
    ]

admin.site.register(Link, LinkAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Page, PageAdmin)
