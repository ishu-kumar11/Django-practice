from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(is_deleted=False)
    return render(request, 'easy_audit/task_list.html', {'tasks': tasks})


def task_history(request, pk):
    task = get_object_or_404(Task, pk=pk)
    history = task.history.all()

    changes = []

    for i in range(len(history) - 1):
        new = history[i]
        old = history[i + 1]

        diff = new.diff_against(old)

        field_changes = []
        for change in diff.changes:
            field_changes.append({
                'field': change.field,
                'old': change.old,
                'new': change.new
            })

        changes.append({
            'date': new.history_date,
            'user': new.history_user,
            'type': new.history_type,
            'fields': field_changes
        })

    return render(request, 'easy_audit/task_history.html', {
        'task': task,
        'changes': changes,
        'is_deleted': task.is_deleted
    })


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_deleted = True
    task.save()
    return redirect('task_history', pk=pk)

