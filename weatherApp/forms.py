from django import forms


class NameForm(forms.Form):
    cityName = forms.CharField(label='Enter City Name', max_length=100)
