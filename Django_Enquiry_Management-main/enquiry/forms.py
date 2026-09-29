from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = "__all__"

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Full Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number'
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Subject'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter your enquiry'
            }),

        }