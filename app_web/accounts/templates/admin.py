from django.contrib import admin
from .models import RegisterCandidate,RegisterEmployer,OpenJobs,AppliedJobs

# Register your models here.
admin.site.register(RegisterEmployer)
admin.site.register(RegisterCandidate)
admin.site.register(OpenJobs)
admin.site.register(AppliedJobs)
