from django.db import models
from django.db.models.fields import BooleanField
from django.utils.timezone import now

# Create your models here.
class RegisterCandidate(models.Model):
    email=models.EmailField() 
    name=models.CharField(max_length=20)
    address=models.TextField()
    state=models.TextField()
    pincode=models.IntegerField()
    phoneno=models.IntegerField()
    qualification=models.TextField()
    jobtypes=models.TextField()
    skills=models.TextField()
    experience=models.TextField()

    def __str__(self):
        return self.name

class RegisterEmployer(models.Model):
    email=models.EmailField() 
    company_email=models.EmailField() 
    company_name=models.TextField()
    no_of_vacancies=models.IntegerField()
    name=models.CharField(max_length=20)
    address=models.TextField()
    state=models.TextField()
    pincode=models.IntegerField()
    contactno=models.IntegerField()
    work_hours=models.TextField()
    jobtypes=models.TextField()
    skills=models.TextField()
    salary=models.TextField()
    comments=models.TextField()
    jobname=models.TextField()
    open_date=models.DateTimeField(default=now)
    close_date=models.DateTimeField(default=now)
    isVerified=models.BooleanField(default=False)
    job_closed=models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.company_name)+" - "+str(self.jobname)


class AppliedJobs(models.Model):
    jobname=models.ForeignKey(RegisterEmployer,blank=True,null=True,on_delete=models.SET_NULL)
    name=models.TextField()
    email=models.EmailField()
    apply_date=models.DateTimeField(default=now)

    def __str__(self):
        return str(self.name)+" - "+str(self.jobname)
