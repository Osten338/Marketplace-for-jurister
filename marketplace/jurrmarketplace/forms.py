from django import forms
from .models import Assignment
from .models import Assignment, AssignmentApplication

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'price', 'due_date', 'category']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
class AssignmentApplicationForm(forms.ModelForm):
    class Meta:
        model = AssignmentApplication
        fields = ['proposal', 'bid_amount']
