from django import forms


class QuoteRequestForm(forms.Form):
    structure = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=255)
    email = forms.EmailField()
    telephone = forms.CharField(max_length=50, required=False)
    domaine = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    article = forms.CharField(max_length=255, required=False)

