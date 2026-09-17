from django.contrib import admin
from .models import Project, Service, ServiceImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'year',
        'is_featured',
        'created_at',
    )

    list_filter = (
        'category',
        'year',
        'is_featured',
    )

    search_fields = (
        'title',
        'description',
    )

    list_editable = (
        'is_featured',
    )

    ordering = (
        '-created_at',
    )


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

    fields = (
        'image',
        'caption',
        'order',
    )

    ordering = (
        'order',
        'created_at',
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'number',
        'title',
        'slug',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'title',
        'short_title',
        'description',
        'full_description',
    )

    list_editable = (
        'is_active',
    )

    prepopulated_fields = {
        'slug': ('title',),
    }

    ordering = (
        'number',
        'created_at',
    )

    inlines = [
        ServiceImageInline,
    ]

