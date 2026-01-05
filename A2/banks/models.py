from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=100)
    institution_number = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(User, verbose_name="books",related_name="Book_owner" ,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"
        ordering = ['name']
    
    def __str__(self):
        return self.name
class Branch(models.Model):
    name = models.CharField(max_length=100)
    transit_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,verbose_name="Email Address")
    capacity = models.PositiveIntegerField(null=True,blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    bank = models.ForeignKey(Bank, verbose_name="associated bank",related_name="branches", on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
        ordering = ['bank', 'name']
    def __str__(self):
        return f"{self.name} , {self.transit_number} and {self.bank.name}"
    