import os
from django.shortcuts import render
from django.views import View
from main.forms import *
from main.models import *
from main.utils import get_text_from_image
from django.conf import settings

# Create your views here.
PATH = os.path.join(settings.BASE_DIR, "media")

class Index(View):
    def get(self, request):
        form = NumberPlateForm()
        qs = NumberPlate.objects.all().order_by("-created_at")
        return render(request, "index.html", {'form' : form, "data":qs})
    def post(self, request):
        form = NumberPlateForm(request.POST, request.FILES)
        if form.is_valid():
            # form.plate_image.data
            form.save() 
        num_obj = NumberPlate.objects.order_by("-created_at").first()
        if num_obj:
            try:
                img_name = get_text_from_image(num_obj.plate_image.path, True).upper()
            except Exception as e:
                print(str(e))
                img_name = ""
            num_obj.name = img_name
            num_obj.save()
        qs = NumberPlate.objects.all().order_by("-created_at")
        return render(request, 'index.html', {'form' : form, "data":qs})

        
