from django.contrib import admin

from .models import ExceptionLog


@admin.register(ExceptionLog)
class ExceptionLogAdmin(admin.ModelAdmin):
    fields = [
        "created_at",
        "level",
        "subject",
        "logger_name",
        "path_name",
        "func_name",
        "line_num",
        "traceback"
    ]
    readonly_fields = fields
    list_display = [
        "created_at",
        "level",
        "subject",
        "logger_name",
        "path_name",
        "func_name",
        "line_num"
    ]
    list_filter = [
        "created_at",
        "level",
        "logger_name"
    ]

    def has_delete_permission(self, request, obj=None):
        """
        Disabling the delete permissions
        """
        return True

    def has_add_permission(self, request):
        """
        Disabling the create permissions
        """
        return False
