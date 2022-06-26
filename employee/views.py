from django.shortcuts import render, HttpResponseRedirect
from .forms import EmployeeRegistration
from .models import User
# Create your views here.

# This function will add new item and show all
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
           nm = fm.cleaned_data['name']
           em = fm.cleaned_data['email']
           rl = fm.cleaned_data['role']
           slr = fm.cleaned_data['salary']
           ct = fm.cleaned_data['city']
           dob = fm.cleaned_data['dob']
       
           reg = User(name=nm, email=em, role=rl,salary=slr,city=ct,dob=dob)
           reg.save()
           fm = EmployeeRegistration()
    else:
        fm = EmployeeRegistration()
    empl = User.objects.all()
    return render(request, 'employee/addandshow.html',{'form':fm, 'emp':empl})

# This function update/edit data
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(instance=pi)

    return render(request,'employee/update.html',{'form':fm})

# This function will delete data
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
            
