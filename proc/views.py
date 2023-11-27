from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
     if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        print(name)
        # print(uploaded_file.size)
     return render(request, "index.html")

