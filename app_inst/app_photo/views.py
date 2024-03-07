from django.shortcuts import render

from forms import PictureForm
from models import Picture

# Create your views here.


def index(request):
    return render(request, template_name="app_photo/index.html", context={"msg": "Hello world"})


def pictures(request):
    return render(request, template_name="app_photo/pictures.html", context={})


def upload(request):
    form = PictureForm(instance=Picture())
    return render(request, template_name="app_photo/upload.html", context={"form": form})
