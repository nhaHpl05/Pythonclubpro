from django.shortcuts import render, get_object_or_404
from .models import Resource
from .models import Meeting

# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')

def getResource(request):
    resource_list = Resource.objects.all()
    return render(request,'pythonclubapp/resource.html',{'resource_list' : resource_list})

def getMeeting(request):
    meeting_list= Meeting.objects.all()
    return render(request, 'pythonclubapp/meeting.html', {'meeting_list': meeting_list})

def getMeetingDetails(request, id):
    meet_details=get_object_or_404(Meeting, pk=id)
    context={
        'meet_details': meet_details
    }

    return render(request, 'pythonclubapp/meetingdetails.html', context = context)
