from rest_framework import serializers
from database.models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'department_id')


class ServiceSerializerGet(serializers.ModelSerializer):
    department = serializers.CharField(source='department_id.name')

    class Meta:
        model = Service
        fields = ('id', 'name', 'department_id', 'department')


class GuardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guard
        fields = ('id', 'name', 'type', 'duration_hs', 'service_id')


class GuardSerializerGet(serializers.ModelSerializer):
    department = serializers.CharField(source='service_id.department_id.name')
    service = serializers.CharField(source='service_id.name')

    class Meta:
        model = Guard
        fields = ('id', 'name', 'type', 'duration_hs', 'service_id', 'service', 'department')


class ShiftSerializerGet(serializers.ModelSerializer):
    department = serializers.CharField(source='service_id.department_id.name')
    service = serializers.CharField(source='service_id.name')

    class Meta:
        model = Guard
        fields = ('id', 'name', 'type', 'duration_hs', 'service', 'department')


class PersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personal
        fields = ('id', 'name', 'last_name', 'profession', 'phone', 'service_id')


class PersonalSerializerGet(serializers.ModelSerializer):
    department = serializers.CharField(source='service_id.department_id.name')
    service = serializers.CharField(source='service_id.name')

    class Meta:
        model = Personal
        fields = ('id', 'name', 'last_name', 'profession', 'phone', 'is_pro', 'service', 'department')


class GuardSheetSerializerGet(serializers.ModelSerializer):
    service = serializers.CharField(source='guard_id.service_id.name')
    personal_name = serializers.CharField(source='personal_id.name')
    personal_last_name = serializers.CharField(source='personal_id.last_name')
    guard = serializers.CharField(source='guard_id.name')

    class Meta:
        model = GuardSheet
        fields = ('id', 'date', 'guard_id', 'personal_id', 'service', 'personal_name', 'personal_last_name', 'guard')


class GuardSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuardSheet
        fields = ('id', 'date', 'guard_id', 'personal_id')
