from django import forms

class JournalFoam(forms.Form):
    title = forms.CharField(label="journal form", max_length=200)
    content = forms.CharField(widget= forms.Textarea)