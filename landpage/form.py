from django import forms

from .models import LandModel

class LandForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Felipe Martins", "id":"name"}))
    whatsapp = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"(11) 91001-1001", "id":"whatsapp"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"FelipeMartins@gmail.com", "id":"email"}))

    class Meta:
        model = LandModel
        fields = ['name', 'whatsapp', 'email']
        