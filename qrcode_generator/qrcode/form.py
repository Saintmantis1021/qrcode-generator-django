from django import forms
from .models import  qrcode
from django.forms import ClearableFileInput, FileInput




class QRcodeForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(QRcodeForm, self).__init__(*args, **kwargs)
    
     class Meta:
        model = qrcode
        labels = {
            
            'qrcodeInput': 'Enter the Text',
        }
        fields = ['qrcodeInput']

        widgets = {
            'id':'btn3',
            
        }
 