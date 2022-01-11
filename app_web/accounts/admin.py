from django.contrib import admin
from .models import RegisterCandidate,RegisterEmployer,AppliedJobs
# Register your models here.
admin.site.register(RegisterEmployer)
admin.site.register(RegisterCandidate)
admin.site.register(AppliedJobs)

