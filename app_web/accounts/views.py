
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import RegisterCandidate,RegisterEmployer,AppliedJobs
from django.views.defaults import page_not_found
import datetime
from django.db.models import Q


# Create your views here.
@login_required(login_url='login')
def candidate_register(request):
    if request.method=='POST':
        email=request.POST['email'] 
        name=request.POST['name']
        address=request.POST['address']
        state=request.POST['state']
        pincode=request.POST['pincode']
        qualification=request.POST['qualification']
        jobtypes=request.POST['jobtypes']
        skills=request.POST['skills']
        experience=request.POST['experience']
        # comments=request.POST['comments']
        phoneno=request.POST['phoneno']

        candidate_object=RegisterCandidate(email=email,name=name,address=address,state=state,pincode=pincode,qualification=qualification,
        jobtypes=jobtypes,skills=skills,experience=experience,phoneno=phoneno)

        if candidate_object is not None:
            candidate_object.save()
            messages.success(request,"Successfully Registered for a job!!")
            return redirect("/")
        else:
            messages.error(request,"invalid form data submitted!!")
            return redirect("candidate_register")

    return render(request,'accounts/candidate_register.html')


@login_required(login_url='login')
def employer_register(request):
    if request.method=='POST':
        email=request.POST['email'] 
        company_email=request.POST['company_email'] 
        name=request.POST['name']
        address=request.POST['address']
        state=request.POST['state']
        pincode=request.POST['pincode']
        salary=request.POST['salary']
        jobtypes=request.POST['jobtypes']
        skills=request.POST['skills']
        work_hours=request.POST['work_hours']
        comments=request.POST['comments']
        contactno=request.POST['contactno']
        no_of_vacancies=request.POST['no_of_vacancies']
        company_name=request.POST['company_name']
        jobname=request.POST['jobname']
        open_date=request.POST['open_date']
        close_date=request.POST['close_date']
        

        employer_object=RegisterEmployer(email=email,company_email=company_email,name=name,address=address,state=state,pincode=pincode,salary=salary,
        jobtypes=jobtypes,skills=skills,work_hours=work_hours,comments=comments,contactno=contactno,no_of_vacancies=no_of_vacancies,company_name=company_name,jobname=jobname,
        open_date=open_date,close_date=close_date)

        if employer_object is not None:
            employer_object.save()
            messages.success(request,"Successfully Registered for Hiring!!")
            return redirect("/")
        else:
            messages.error(request,"invalid form data submitted!!")
            return redirect("employer_register")

    return render(request,'accounts/employer_register.html')
    

def register(request):
    if request.method=='POST':
        email=request.POST['email']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request,"username taken!!")
            return redirect("accounts/register")

        elif User.objects.filter(email=email).exists():
            messages.error(request,"email already taken!!")
            return redirect("register")
        else:

            if password1==password2:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                if user is not None:
                    user.save()
                    messages.success(request,"User created successfully!!")
                    return redirect("login")
                else:
                    messages.error(request,"Some Error in Entered Fileds! Try Again!")
                    return redirect("register")
            else:
                messages.error(request,"Passwords do not match!!")
                return redirect("register")
    else:
        return render(request,'accounts/register.html') 

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        try:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,"successfully logged in!!")
                return redirect("dashboard")
            else:
                username=User.objects.get(email=username.lower()).username
                user=auth.authenticate(username=username,password=password)
                auth.login(request,user)
                messages.success(request,"successfully logged in!!")
                return redirect("dashboard")
        except:
               messages.error(request,"invalid credentials!!")
               return redirect("login")

    return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request) 
    messages.success(request,"successfully logged out!!")
    return redirect("/")

def handler404(request, exception):
        return page_not_found(request, exception, template_name="accounts/404.html")

@login_required(login_url='login')
def dashboard(request):
    current_user=request.user
    email=current_user.email
    jobs=RegisterEmployer.objects.all() 

    applied_list=AppliedJobs.objects.filter(email=email).values_list('id',flat=True)
    applied_list=list(applied_list)
    no_of_jobs=len(applied_list)

    if jobs is not None:
        return render(request,'accounts/dashboard.html',{'jobs':jobs,'applied_list':applied_list,'no_of_jobs':no_of_jobs})
    else:
        return render(request,'accounts/dashboard.html',{'applied_list':applied_list,'no_of_jobs':no_of_jobs})

@login_required(login_url='login')
def applied(request,id): 
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        job_applied=RegisterEmployer.objects.get(id=id) 

        applied=AppliedJobs.objects.filter(email=email).filter(jobname=job_applied) 

        if applied.exists():
            messages.error(request,"Already Applied for this job!")
            return redirect("dashboard")
        else:

            if job_applied is not None:
                applied_job=AppliedJobs(jobname=job_applied,name=name,email=email) 
                applied_job.save() 
                print(job_applied)
                return render(request,"accounts/applied.html",{"applied_job":job_applied}) 
            else:
                messages.error(request,"Error in applying for the Job!") 
                return redirect("dashboard")




