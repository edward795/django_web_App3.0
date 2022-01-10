from django.db import models

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
    comments=models.TextField()

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

class OpenJobs(RegisterEmployer):
    isVerified=models.BooleanField(default=False)

    def __str__(self):
        return self.email