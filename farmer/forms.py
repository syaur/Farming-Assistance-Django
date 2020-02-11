from django import forms
from .models import Contactus

class AddContactusForm(forms.ModelForm):
	class Meta:
		model = Contactus
		fields = ('__all__')