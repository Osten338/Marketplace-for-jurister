from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Lawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=255)  # Add this line for the category field
    due_date = models.DateField()  # Add this line for the due_date field

    def __str__(self):
        return self.title

class AssignmentApplication(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(User, on_delete=models.CASCADE)
    proposal = models.TextField()
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('assignment', 'lawyer')
