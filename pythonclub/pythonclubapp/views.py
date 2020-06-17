from django.shortcuts import render, get_object_or_404
from .models import Resource
from .models import Meeting
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

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
@login_required
def FormMeeting(request):
    form = MeetingForm
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'pythonclubapp/meetingform.html', {'form': form})
@login_required
def FormResource(request):
    form = ResourceForm
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'pythonclubapp/resourceform.html', {'form': form})

def loginmessage(request):
    return render(request, 'pythonclubapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'pythonclubapp/logoutmessage.html')



    



