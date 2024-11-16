import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from .models import Department
from .models import JobPosition

# Endpoint base de tu API Spring Boot
SPRING_BOOT_API_URL = "http://localhost:8080/api/rrhh_module"


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



def list_departments(request):
    try:
        # Realiza una solicitud GET al endpoint de Spring Boot
        response = requests.get(f"{SPRING_BOOT_API_URL}/departments/all")
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP

        # Obtén los datos de la respuesta en formato JSON
        departments = response.json()
        return render(request, 'department.html', {'departments': departments})

    except requests.exceptions.RequestException as e:
        # Manejo de errores: en caso de que la solicitud a la API falle
        return JsonResponse({'error': 'Error al conectarse con el servicio de departamentos'}, status=500)


def list_job_positions(request):
    try:
        response = requests.get(f"{SPRING_BOOT_API_URL}/jobPositions/all")
        response.raise_for_status()  

        job_positions = response.json()
        return render(request, 'job_position.html', {'job_positions': job_positions})

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': 'Error al conectarse con el servicio de puestos de trabajo'}, status=500)
    
# Vistas para Employee
def list_employees(request):
    try:
        response = requests.get(f"{SPRING_BOOT_API_URL}/employees/all")
        response.raise_for_status()

        employees = response.json()
        return render(request, 'employee.html', {'employees': employees})
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error al conectar con el servicio de empleados: {str(e)}'}, status=500)


# Vistas para SalaryHistory
def list_salary_histories(request):
    try:
        response = requests.get(f"{SPRING_BOOT_API_URL}/salaryHistories/all")
        response.raise_for_status()

        salary_histories = response.json()
        return render(request, 'salary_history.html', {'salary_histories': salary_histories})
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error al conectar con el servicio de historial de salarios: {str(e)}'}, status=500)


# Vistas para PaymentDate
def list_payment_dates(request):
    try:
        response = requests.get(f"{SPRING_BOOT_API_URL}/paymentDates/all")
        response.raise_for_status()

        payment_dates = response.json()
        return render(request, 'payment_date.html', {'payment_dates': payment_dates})
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error al conectar con el servicio de fechas de pago: {str(e)}'}, status=500)


# Vistas para Vacation
def list_vacations(request):
    try:
        response = requests.get(f"{SPRING_BOOT_API_URL}/vacations/all")
        response.raise_for_status()

        vacations = response.json()
        return render(request, 'vacation.html', {'vacations': vacations})
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error al conectar con el servicio de vacaciones: {str(e)}'}, status=500)