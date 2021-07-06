from django import forms

class Contact_form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field-box'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field-box sa'}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input-field-box'}), required=True)
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field-box'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-field-box', 'rows': '10', 'cols': '50'}), required=True)
