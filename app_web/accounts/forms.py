from .models import RegisterCandidate
from django.forms import ModelForm

class RegisterCandidateForm(ModelForm):
    class Meta:
        model=RegisterCandidate
        fields="__all__"
