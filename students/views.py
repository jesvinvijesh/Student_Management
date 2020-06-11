from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from students.models import student


def index(request):
    s = student.objects.all()
    return render(request,'index.html', {'student': s})
