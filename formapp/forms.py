from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=20,label='Enter the name')
    age=forms.IntegerField(label='Enter the age')
    gender=forms.CharField(max_length=10,label='Enter the gender')
    created_at=forms.DateField(label='Enter the date')