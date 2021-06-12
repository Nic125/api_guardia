from django.db import models

from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name


class Guard(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    duration_hs = models.CharField(max_length=11)
    service_id = models.ForeignKey(Service, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Guardia"
        verbose_name_plural = "Guardias"

    def __str__(self):
        return self.name


class Personal(models.Model):
    file = models.CharField(max_length=30, unique=True)
    d = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, unique=True)
    is_pro = models.CharField(max_length=10)
    is_active = models.CharField(max_length=10, default='yes')
    service_id = models.ForeignKey(Service, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"

    def __str__(self):
        return self.last_name + ", " + self.name + " - " + self.service_id.name


class GuardSheet(models.Model):
    date = models.DateField()
    is_working_day = models.CharField(max_length=25)
    is_active = models.CharField(max_length=10, default="no")
    shift = models.CharField(max_length=20, default="24")
    is_extra = models.CharField(max_length=10, default="no")
    guard_id = models.ForeignKey(Guard, on_delete=models.PROTECT)
    personal_id = models.ForeignKey(Personal, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Planilla guardia"
        verbose_name_plural = "Planillas guardias"

    def __str__(self):
        return self.date


class NotWorkingDays(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=70)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Día no laborable"
        verbose_name_plural = "Días no laborables"

    def __str__(self):
        return self.name


class Licences(models.Model):
    name = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Licencia"
        verbose_name_plural = "Licencias"

    def __str__(self):
        return self.name


