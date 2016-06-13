from django import forms
from .models import Post
from django.forms import ModelForm, DateInput, DateField, extras
from django.forms.extras.widgets import SelectDateWidget

class PostForm(forms.ModelForm):
	display_date = forms.DateField(widget=extras.SelectDateWidget)
	godzina = forms.TimeField()

	class Meta:
		model = Post
		fields = ('title', 'text', 'display_date', 'godzina', 'image')
		

