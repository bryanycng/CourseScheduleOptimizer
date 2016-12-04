from django import forms

class indexForm(forms.Form):
    course1 = forms.ChoiceField(choices=[(x,x) for x in range(1, 32)])
    course2 = forms.ChoiceField(choices=[(x,x) for x in range(1, 32)])
    course3 = forms.ChoiceField(choices=[(x,x) for x in range(1, 32)])
    course4 = forms.ChoiceField(choices=[(x,x) for x in range(1, 32)])
    course5 = forms.ChoiceField(choices=[(x,x) for x in range(1, 32)])
    course6 = forms.ChoiceField(choices=[(x,x) for x in range(1, 32)])
    course7 = forms.ChoiceField(choices=[(x,x) for x in range(1, 32)])
    course8 = forms.ChoiceField(choices=[(x,x) for x in range(1, 32)])