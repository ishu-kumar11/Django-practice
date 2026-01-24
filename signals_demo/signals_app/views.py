from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, SignalLog

def task_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')

    tasks = Task.objects.all()
    logs = SignalLog.objects.order_by('-created_at')[:10]

    return render(request, 'signals_app/task_list.html', {
        'tasks': tasks,
        'logs': logs
    })


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()   # 👈 THIS LINE TRIGGERS DELETE SIGNALS
    return redirect('task_list')