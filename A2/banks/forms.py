from django import forms
from .models import Bank,Branch

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'description', 'institution_number', 'swift_code']
        widgets = {
            'institution_number': forms.TextInput(attrs={'placeholder': 'Institution Number'}),
            'swift_code': forms.TextInput(attrs={'placeholder': 'SWIFT Code'}),
        }
class BranchForm(forms.ModelForm):
    class Meta:
        models = Branch
        fields = ['name', 'transit_number', 'address', 'email', 'capacity']
        widgets = {
            'email': forms.EmailInput(attrs={'value': 'admin@enigmatix.io'}),
        }
