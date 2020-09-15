from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.
def addshow(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            registration = User(name=name, email=email, password=password)
            registration.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    student = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': form, 'student': student})

def update_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  fm = StudentRegistration(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()
 else:
  pi = User.objects.get(pk=id)
  fm = StudentRegistration(instance=pi)
 return render(request, 'enroll/updatestudent.html', {'form':fm})

def delete_data(request, id):
    if request.method == 'POST':
        dele = User.objects.get(pk=id)
        dele.delete()
        return HttpResponseRedirect('/')

