from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Meeting(models.Model):
    meeting_title = models.CharField(max_length=255)
    meeting_date = models.DateField()
    meeting_time = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    def __str__(self):
        return self.meeting_title

    class Meta:
        db_table='meeting'
        verbose_name_plural='meeting'

class MeetingMinutes(models.Model):
    meeting_id = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutes_text = models.TextField()

    def __str__(self):
        return self.meeting_id

class Resource(models.Model):
    resource_name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=255)
    URL = models.URLField()
    date_entered = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()

    def __str__(self):
        return self.Resource
    
class Event(models.Model):
    event_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.CharField(max_length=255)
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.event_title



    
