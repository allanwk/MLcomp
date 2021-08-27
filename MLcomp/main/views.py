from django.shortcuts import render
from main.models import Dataset

def homepage(request):
    return render(request, 
                  template_name="./main/homepage.html",
                  context={"datasets": Dataset.objects.all})

def dataset(request, id):
    return render(request, 
                  template_name="./main/dataset.html",
                  context={"dataset": Dataset.objects.get(id=id)})