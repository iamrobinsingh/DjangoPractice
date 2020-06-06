from django import  forms

class studentFeedback(forms.Form):
    name = forms.CharField(label ='Name:')
    age = forms.IntegerField(label ='Age:')
    rollNo = forms.IntegerField(label ='Roll-No:')
    email = forms.EmailField(label='E-Mail:')
    feedback = forms.CharField(widget= forms.Textarea, label ='Feedback:')
