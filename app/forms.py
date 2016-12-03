from django import forms

class index(forms.Form):
    course1 = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])