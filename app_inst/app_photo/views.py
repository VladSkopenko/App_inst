from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, template_name="app_photo/index.html", context={"msg": "Hello world"})
