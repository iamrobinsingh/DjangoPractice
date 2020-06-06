from django import  forms
from django.core import validators


def starts_with(value):
    if value[0] !='r':
        raise forms.ValidationError("Name Should start with 'r'")
    return value


class studentFeedback(forms.Form):
    name = forms.CharField(label ='Name:', validators=[starts_with])
    age = forms.IntegerField(label ='Age:')
    rollNo = forms.IntegerField(label ='Roll-No:')
    email = forms.EmailField(label='E-Mail:')
    feedback = forms.CharField(widget= forms.Textarea, label ='Feedback:',validators=[validators.MaxLengthValidator(15),validators.MinLengthValidator(5)])


    # def clean_name(self):
    #     inputname = self.cleaned_data['name']
    #     if inputname not in ['robin','aastha','utkarsh']:
    #         raise forms.ValidationError("Not allowed to submit feedback")
    #     return inputname

    # At single time you can validate forms

    def clean(value):
        cleaned_data = super().clean()
        inputname = cleaned_data['name']
        if len(inputname) >6:
            raise forms.ValidationError("Name should be less then 6 Letter")
        inputrollno = cleaned_data['rollNo']
        if len(str(inputrollno))!=4:
            raise forms.ValidationError("Roll No should be 4 digit long")
