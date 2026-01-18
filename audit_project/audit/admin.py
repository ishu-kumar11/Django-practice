from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'model_name', 'object_id', 'ip_address', 'timestamp')
    readonly_fields = ('ip_address', 'timestamp')

    def save_model(self, request, obj, form, change):
        if not obj.ip_address:
            obj.ip_address = self.get_client_ip(request)
        super().save_model(request, obj, form, change)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
