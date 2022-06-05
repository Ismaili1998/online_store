from django.shortcuts import render
from .forms import TrialForm, ContactForm
from django.contrib import messages 
# Create your views here.


def trial(request):
    if request.method == "POST":
        form = TrialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'done successfully !.')
        else:
            messages.error(request, 'error , please retry !.')

    form = TrialForm()
    return render(request,'trial.html',{"form":form})   
    
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'done successfully !.')
        else:
            messages.error(request, 'error , please retry !.')
        
    form = ContactForm()
    return render(request,'contact.html',{"form":form})   