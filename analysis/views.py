from django.shortcuts import render
from .models import SocialData
from .forms import SocialForm

import pickle
model = pickle.load(open('social_ads.suv','rb'))

def home(request,result=None):
    if request.method=='POST':
        form=SocialForm(request.POST)
        

        if form.is_valid():
             my_form = form.save(commit=False)
             gender=form.cleaned_data['gender']
             age=form.cleaned_data['age']
             salary=form.cleaned_data['salary']
             if gender=='Male':
                gender=1
             else:
                gender=0    
             data=[[age,salary,gender]]
             result=model.predict(data)
             if result[0]==0:
                 result='not subscribe'
             else:
                 result='subscribe'    
    else:    
        form=SocialForm()     
    return render(request,'home.html',{'form':form,'result':result})

# Create your views here.
