from django import forms
from django.forms import ModelForm
from django.forms import Textarea
from studentSelection.models import students


class studentRegisterForm (ModelForm) :

    class Meta:
        model = students
        fields = ['studentCode','password','firstName','lastName','mobile','email','img','address']
        widgets = {
            'address': Textarea(attrs={'cols': 10, 'rows': 2}),
        }



    def clean_recipients(self):
        data = self.cleaned_data['studentCode']
        if not data:
            raise forms.ValidationError("You have forgotten about Fred!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data