from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import *
from database.serializers import *


@csrf_exempt
def department(request, id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Departamento creado con éxito", safe=False)
        return JsonResponse("Error al crear el departamento", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(id=department_data['id'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Departamento actualizado con éxito", safe=False)
        return JsonResponse("Error al actualizar el departamento", safe=False)
    elif request.method == "DELETE":
        department = Department.objects.get(id=id)
        department.delete()
        return JsonResponse("Departamento eliminado con éxito", safe=False)


@csrf_exempt
def service(request, id=0):
    if request.method == 'GET':
        service = Service.objects.all()
        service_serializer = ServiceSerializerGet(service, many=True)
        return JsonResponse(service_serializer.data, safe=False)
    elif request.method == 'POST':
        service_data = JSONParser().parse(request)
        service_serializer = ServiceSerializer(data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse("Servicio creado con éxito", safe=False)
        return JsonResponse("Error al crear el servicio", safe=False)
    elif request.method == 'PUT':
        service_data = JSONParser().parse(request)
        service = Service.objects.get(id=service_data['id'])
        service_serializer = ServiceSerializer(service, data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse("Servicio actualizado con éxito", safe=False)
        return JsonResponse("Error al actualizar el servicio", safe=False)
    elif request.method == "DELETE":
        service = Service.objects.get(id=id)
        service.delete()
        return JsonResponse("Servicio eliminado con éxito", safe=False)


@csrf_exempt
def guard(request, id=0):
    if request.method == 'GET':
        guard = Guard.objects.all()
        shift_serializer = GuardSerializerGet(guard, many=True)
        return JsonResponse(shift_serializer.data, safe=False)
    elif request.method == 'POST':
        guard_data = JSONParser().parse(request)
        guard_serializer = GuardSerializer(data=guard_data)
        if guard_serializer.is_valid():
            guard_serializer.save()
            return JsonResponse("La guardia / turno se a creado con éxito", safe=False)
        return JsonResponse("Error al crear la guardia / turno", safe=False)
    elif request.method == 'PUT':
        guard_data = JSONParser().parse(request)
        guard = Guard.objects.get(id=guard_data['id'])
        guard_serializer = GuardSerializer(guard, data=guard_data)
        if guard_serializer.is_valid():
            guard_serializer.save()
            return JsonResponse("La guardia / turno se a actualizado con éxito", safe=False)
        return JsonResponse("Error al actualizar la guardia / turno", safe=False)
    elif request.method == "DELETE":
        guard = Guard.objects.get(id=id)
        guard.delete()
        return JsonResponse("La guardia / turno se a eliminado con éxito", safe=False)


@csrf_exempt
def personal(request, id=0):
    if request.method == 'GET':
        personal = Personal.objects.all()
        personal_serializer = PersonalSerializerGet(personal, many=True)
        return JsonResponse(personal_serializer.data, safe=False)
    elif request.method == 'POST':
        personal_data = JSONParser().parse(request)
        personal_serializer = PersonalSerializer(data=personal_data)
        if personal_serializer.is_valid():
            personal_serializer.save()
            return JsonResponse("La persona se a creado con éxito", safe=False)
        return JsonResponse("Error al crear la persona", safe=False)
    elif request.method == 'PUT':
        personal_data = JSONParser().parse(request)
        personal = Personal.objects.get(id=personal_data['id'])
        personal_serializer = PersonalSerializer(personal, data=personal_data)
        if personal_serializer.is_valid():
            personal_serializer.save()
            return JsonResponse("La persona se a actualizado con éxito", safe=False)
        return JsonResponse("Error al actualizar la persona", safe=False)
    elif request.method == "DELETE":
        personal = Personal.objects.get(id=id)
        personal.delete()
        return JsonResponse("La persona se a eliminado con éxito", safe=False)


@csrf_exempt
def guard_sheet(request, id=0):
    if request.method == 'GET':
        guard_sheet = GuardSheet.objects.all()
        guard_sheet_serializer = GuardSheetSerializerGet(guard_sheet, many=True)
        return JsonResponse(guard_sheet_serializer.data, safe=False)
    elif request.method == 'POST':
        guard_sheet_data = JSONParser().parse(request)
        guard_sheet_serializer = GuardSheetSerializer(data=guard_sheet_data)
        if guard_sheet_serializer.is_valid():
            guard_sheet_serializer.save()
            return JsonResponse("La planificación se a creado con éxito", safe=False)
        return JsonResponse("Error al crear la planificación", safe=False)
    elif request.method == 'PUT':
        guard_sheet_data = JSONParser().parse(request)
        guard_sheet = GuardSheet.objects.get(id=guard_sheet_data['id'])
        guard_sheet_serializer = GuardSheetSerializer(guard_sheet, data=guard_sheet_data)
        if guard_sheet_serializer.is_valid():
            guard_sheet_serializer.save()
            return JsonResponse("La planificación se a actualizado con éxito", safe=False)
        return JsonResponse("Error al actualizar la planificación", safe=False)
    elif request.method == "DELETE":
        guard_sheet = GuardSheet.objects.get(id=id)
        guard_sheet.delete()
        return JsonResponse("La planificación se a eliminado con éxito", safe=False)
