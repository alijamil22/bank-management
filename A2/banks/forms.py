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
        def clean(self):
            cleaned_data = super().clean()
            
            # Checking all fields are required
            for field_name in ['name','description','institution_number','swift_code']:
                value = cleaned_data.get(field_name)
                if not value:
                    self.add_error(field_name,'This field is required!')
            # checking for maximum length of data entered in field
            for field_name in ['name','description','institution_number','swift_code']:
                value = cleaned_data.get(field_name)
                if value and len(value) > 100:
                    #  Here is contradiction I want to say at most 100 char but assignment 
                    # tell me 200 at most so it is what it is
                    self.add_error(field_name,
                                   f"Ensure this value has at most 200 characters (it has {len(value)}).")
            return cleaned_data
class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'transit_number', 'address', 'email', 'capacity']
        widgets = {
            'email': forms.EmailInput(attrs={'value': 'admin@enigmatix.io'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        # Again checking all field require and except capacity field
        for field_name in ['name', 'transit_number', 'address', 'email']:
            value = cleaned_data.get(field_name)
            if not value:
                self.add_error(field_name,"This field is required!")
        for field_name in ['name', 'transit_number', 'address', 'email']:
            # Again checking for max length
            value = cleaned_data.get(field_name)
            if value and len(value) > 100:
                self.add_error(field_name,f"Ensure this value has at most 200 characters (it has {len(value)}).")
        capacity = self.cleaned_data.get('capacity')
        if capacity is not None and capacity < 0:
            self.add_error('capacity','Ensure this value is greater than or equal to zero!')
        return cleaned_data