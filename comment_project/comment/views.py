from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm

# Create your views here.

def comment_list(request):
	comments = Comment.objects.filter(parent=None).order_by('created_at')
	form = CommentForm()

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			parent_id = request.POST.get('parent_id')
			comment = form.save(commit=False)

			if parent_id:
				comment.parent = Comment.objects.get(id=parent_id)

			comment.save()
			return redirect('comments')

	return render(request, 'comment/comment_list.html', {'comments':comments, 'form':form})


def comment_delete(request, id):
	comment = get_object_or_404(Comment, id=id)
	comment.delete()
	return redirect('comments')

def comment_edit(request, id):
	comment = get_object_or_404(Comment, id=id)
	form = CommentForm(instance=comment)

	if request.method == "POST":
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return redirect('comments')

	return render(request, 'comment/edit.html', {'form': form})

