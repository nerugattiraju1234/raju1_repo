from django.shortcuts import render
from firstapp.models import Employee

# Create your views here.
def empview(request):
    emp_list=Employee.objects.all()
    my_dict={"emp_list":emp_list}
    return render(request,"firstapp/home.html",context=my_dict)
