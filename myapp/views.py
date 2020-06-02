from django.shortcuts import render
from .models import Student
from django.views.generic import ListView
from django.views.generic import DeleteView

# Create your views here.

class StudentView(ListView):
    model=Student

class StudentDelete(DeleteView):
	model=Student
	success_url='/'
