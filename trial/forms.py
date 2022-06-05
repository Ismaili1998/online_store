from django import forms
from .models import Trial, Contact

class TrialForm(forms.ModelForm):
    class Meta:
        model = Trial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TrialForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'option':
                self.fields[field].widget.attrs['class'] = 'form-control'
           

    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'