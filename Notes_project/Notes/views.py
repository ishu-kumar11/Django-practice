from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notes
from .forms import NoteForm

# ✅ READ: show only logged-in user's notes
@login_required
def note_list(request):
    notes = Notes.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'Notes/note_list.html', {'notes': notes})


# ✅ CREATE
@login_required
def add_note(request):
    form = NoteForm()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # ✅ important
            note.save()
            return redirect('note_list')

    return render(request, 'Notes/add_note.html', {'form': form})


# ✅ UPDATE (Only owner allowed)
@login_required
def edit_note(request, pk):
    note = get_object_or_404(Notes, pk=pk, user=request.user)  
    # ✅ ensures only owner can edit

    form = NoteForm(instance=note)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')

    return render(request, 'Notes/edit_note.html', {'form': form})


# ✅ DELETE (Only owner allowed)
@login_required
def delete_note(request, pk):
    note = get_object_or_404(Notes, pk=pk, user=request.user)

    if request.method == "POST":
        note.delete()
        return redirect('note_list')

    return render(request, 'Notes/delete_note.html', {'note': note})
