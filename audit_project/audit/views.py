from django.shortcuts import render
from .models import AuditLog

def audit_log_list(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'audit/audit_logs.html', {'logs': logs})
