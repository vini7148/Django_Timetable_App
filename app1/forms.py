from django import forms

# class clform(forms.Form):
#     clno = forms.IntegerField()
#     clse = forms.CharField(max_length=1)
#     cltime = forms.CharField(max_length=50)

class tform(forms.Form):
    tid = forms.IntegerField()

class clform(forms.Form):
    email = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    contribution_credit = forms.BooleanField(required=True)
    agreement = forms.BooleanField(required=True)
    country = forms.CharField(max_length=50)