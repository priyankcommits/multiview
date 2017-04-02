from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from forms import ImageDetailForm
from models import ImageDetail
from utils import compare_images, handle_image_upload
# Create your views here.


@login_required
def home(request):
    template = 'multiview_app/home.html'
    if request.method == 'GET':
        context = {
            'form': ImageDetailForm()
        }
        return render(request, template, context)
    if request.method == 'POST':
        form = ImageDetailForm(request.POST, request.FILES)
        if form.is_valid():
            images = ImageDetail.objects.all()
            handle_image_upload(request, request.FILES.get('image'))
            for image in images:
                image.mse, image.ssim = compare_images(
                    'temp_images/' + str(request.user.id) + '/temp.jpg', 'media/' + str(image.image.name)
                )
        context = {
            'form': ImageDetailForm(),
            'images': images,
        }
        return render(request, template, context)


@login_required
def image_upload(request):
    template = 'multiview_app/upload_image.html'
    if request.method == 'GET':
        image_form = ImageDetailForm()
        context = {
            'form': image_form,
        }
        return render(request, template, context)

    if request.method == 'POST':
        form = ImageDetailForm(request.POST, request.FILES)
        if form.is_valid():
            image_object = ImageDetail()
            image_object.image = form.cleaned_data['image']
            image_object.uploaded_by = request.user
            image_object.name = request.FILES['image'].name
            image_object.save()
            return HttpResponseRedirect(reverse('multiview_app:home'))
        else:
            return render(request, template, context)


@login_required
def images(request):
    template = 'multiview_app/images.html'
    if request.method == 'GET':
        images = ImageDetail.objects.all()
        context = {
            'images': images,
        }
        return render(request, template, context)
