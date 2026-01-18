from django.shortcuts import render
from .models import AuditLog
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def audit_log_list(request):
    logs = AuditLog.objects.all().order_by('-timestamp')

    user = request.GET.get('user')
    action = request.GET.get('action')
    date = request.GET.get('date')

    if user:
        logs = logs.filter(user__username__icontains=user)

    if action:
        logs = logs.filter(action__icontains=action)

    if date:
        logs = logs.filter(timestamp__date=date)

    return render(request, 'audit/audit_logs.html', {
        'logs': logs
    })