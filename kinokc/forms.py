from django import forms
from .models import Post, SignUp, Reservation
from django.forms import ModelForm, DateInput, DateField, CharField, TextInput, extras
from django.forms.extras.widgets import SelectDateWidget

class PostForm(forms.ModelForm):
	display_date = forms.DateField(widget=extras.SelectDateWidget)
	godzina = forms.TimeField()

	class Meta:
		model = Post
		fields = ('title', 'text', 'display_date', 'godzina', 'image')
		
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ('email',)

class ReservationForm(forms.ModelForm):
	dzień = forms.DateField(widget=extras.SelectDateWidget)
	godzina = forms.TimeField()
	ilość_biletów = CharField(widget=TextInput(attrs={'type':'number'}))

	class Meta:
		model = Reservation
		fields = ('imię', 'nazwisko', 'film', 'dzień', 'godzina', 'ilość_biletów')
