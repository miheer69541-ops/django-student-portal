from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


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


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)

    return render(request,'register.html',{'form':form})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')
