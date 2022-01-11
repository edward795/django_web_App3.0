from django.urls import path
from . import views

urlpatterns=[
    path('candidate_register',views.candidate_register,name="candidate_register"),
    path('employer_register',views.employer_register,name="employer_register"),
    path('register',views.register,name="register"),
    path('dashboard',views.dashboard,name="dashboard"),
    path("applied/<int:id>",views.applied,name="applied"),
    path('login',views.login,name="login"), 
    path("logout",views.logout,name="logout")

]

