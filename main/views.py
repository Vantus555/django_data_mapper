from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Объект общения
connector = Mapper()


def index(request):
    students = connector.getAllStudents()

    return render(request, "main/index.html", context={'students': students})


def add_student(request):
    if request.method == 'POST':
        connector.newStudent(
            request.POST['first_name'],
            request.POST['last_name'],
            request.POST['course'],
        )
    return render(request, 'main/newcourse.html')
