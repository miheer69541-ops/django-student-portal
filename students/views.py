
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request,'home.html',{'students':students})

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    return render(request,'register.html',{'form':form})
    