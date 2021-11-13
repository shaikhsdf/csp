from django.db import models
from django.contrib.auth.models import User, Group

class function(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class sub_function(models.Model):
    id = models.AutoField(primary_key=True)
    fk_function = models.ForeignKey(function, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class designation(models.Model):
    id = models.AutoField(primary_key=True)
    fk_function = models.ForeignKey(function, on_delete=models.CASCADE, null=True, default=None)
    fk_sub_function = models.ForeignKey(sub_function, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class state(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    NORTH = 'N'
    EAST = 'E'
    WEST = 'W'
    SOUTH = 'S'
    REGION_CHOICES = [
        (NORTH, 'North'),
        (EAST, 'East'),
        (WEST, 'West'),
        (SOUTH, 'South'),
    ]
    region = models.CharField(max_length=10, choices=REGION_CHOICES, default=None, null=True)
    def __str__(self):
        return self.name

class location(models.Model):
    id = models.AutoField(primary_key=True)
    fk_state = models.ForeignKey(state, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class sub_location(models.Model):
    id = models.AutoField(primary_key=True)
    fk_state = models.ForeignKey(state, on_delete=models.CASCADE, null=True, default=None)
    fk_location = models.ForeignKey(location, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
        
class user_group(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, default=None, blank=True)
    group = models.ForeignKey( Group, on_delete=models.CASCADE, null=True, default=None, blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=10)
    adhaar = models.CharField(max_length=12)
    def __str__(self):
        return self.first_name + '|' + str(self.group.name)

class candidate(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=10)
    adhaar = models.CharField(max_length=12)
    doj = models.DateField(null=True, blank=True, default=None)
    fk_function = models.ForeignKey(function, on_delete=models.CASCADE, null=True, default=None)
    fk_sub_function = models.ForeignKey(sub_function, on_delete=models.CASCADE, null=True, default=None)
    fk_designation = models.ForeignKey(designation, on_delete=models.CASCADE, null=True, default=None)
    fk_state = models.ForeignKey(state, on_delete=models.CASCADE, null=True, default=None)
    fk_location = models.ForeignKey(location, on_delete=models.CASCADE, null=True, default=None)
    fk_sub_location = models.ForeignKey(sub_location, on_delete=models.CASCADE, null=True, default=None)
    created_by = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    recruiter = models.CharField(max_length=100, default='R001')
    obspoc = models.ForeignKey( user_group, on_delete=models.CASCADE, null=True, default=None)
    status = models.CharField(max_length=100)
    group = models.ForeignKey( Group, on_delete=models.CASCADE, null=True, default=4, blank=True)

    def __str__(self):
        return self.first_name + ' ' + str(self.last_name)