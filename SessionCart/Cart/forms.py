from django import forms

class AddItemForms(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()
