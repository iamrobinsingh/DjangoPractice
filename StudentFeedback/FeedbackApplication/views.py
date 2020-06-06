from django.shortcuts import render
from . import forms


def feedback_view(request):
    form = forms.studentFeedback()
    if request.method =='POST':
        form = forms.studentFeedback(request.POST)
        if form.is_valid():
            print("Feedback is successfully submitted")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['age'])
            print(form.cleaned_data['rollNo'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['feedback'])
            return render(request,'FeedbackApplication/thankYou.html')
    return render(request,'FeedbackApplication/feedback.html',{'form':form})
