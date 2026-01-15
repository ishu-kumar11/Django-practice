from django.shortcuts import render,redirect, get_object_or_404
from .forms import PhotoForm
from .models import Photo

# Create your views here.


def upload_photo(request):
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			photo = form.save()
			return redirect('success', photo.id)
	else:
		form = PhotoForm()

	return render(request, 'gallery/upload.html', {'form':form})


def success(request, id):
	photo = get_object_or_404(Photo, id=id)
	return render(request, 'gallery/success.html', {'photo': photo})

def photo_list(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'gallery/photo_list.html', {'photos': photos})


def photo_detail(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, 'gallery/photo_detail.html', {'photo': photo})
