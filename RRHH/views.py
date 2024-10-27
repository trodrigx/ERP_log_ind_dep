from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

def department(request):
    template = loader.get_template("department.html")
    return HttpResponse(template.render())

def employee(request):
    template = loader.get_template("employee.html")
    return HttpResponse(template.render())

def job_position(request):
    template = loader.get_template("job_position.html")
    return HttpResponse(template.render())

def payment_date(request):
    template = loader.get_template("payment_date.html")
    return HttpResponse(template.render())

def salary_history(request):
    template = loader.get_template("salary_history.html")
    return HttpResponse(template.render())

def vacation(request):
    template = loader.get_template("vacation.html")
    return HttpResponse(template.render())