from django.shortcuts import render, get_object_or_404
from .models import Resource

# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')

def getResource(request):
    resource_list = Resource.objects.all()
    return render(request,'pythonclubapp/resource.html',{'resource_list' : resource_list})


