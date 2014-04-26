from django.contrib import admin
from tasking.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'complete', 'link')
    list_filter = ('state', 'created_at', 'updated_at')
    search_fields = ('name',' description', 'state', 'complete', 'link')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ('Task', {
            'fields': ('name', 'description', 'state', 'complete', 'link')
        }),
        ('Change History', {
            'classes': ('collapse', ),
            'fields': ('created_at', 'updated_at')
        })
    ]

admin.site.register(Task, TaskAdmin)
