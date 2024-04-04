from django.shortcuts import render
from .forms import StudentForm
from .models import StudentData
# Create your views here.
def register(request):
    if request.method=='GET':
        form=StudentForm()
        return render(request,'register.html',{'form':form})
    else:
        form=StudentForm(request.POST)
        if form.is_valid():
            StudentData(
               name=form.cleaned_data['name'],
               age=form.cleaned_data['age'],
               gender=form.cleaned_data['gender'],
               created_at=form.cleaned_data['created_at']
            ).save()
        return render(request,'result.html')