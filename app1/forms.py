from django import forms

class clform(forms.Form):
    clno = forms.IntegerField()
    clse = forms.CharField(max_length=1)
    cltime = forms.CharField(max_length=50)

class tform(forms.Form):
    tid = forms.IntegerField()