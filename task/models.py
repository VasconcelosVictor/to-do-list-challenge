from django.db import models
from django.contrib.auth.models import User 

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    def get_time_record(self):
        return TimeRecord.objects.filter(task=self).first()

class TimeRecord(models.Model):
    registration_date = models.DateField()
    minutes_worked = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    task = models.OneToOneField(Tasks, on_delete=models.CASCADE)

    def convert_minutes(self, ):
        hours =  self.minutes_worked // 60  
        minutes = self.minutes_worked % 60
        if hours == 0:
            horas = "00"
        if minutes == 0:
            minutes = "00"

        return f'{horas}Hs : {minutes}mm'

    



