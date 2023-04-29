from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Assignment
from .forms import AssignmentForm
from .models import AssignmentApplication
from .forms import AssignmentApplicationForm 

# Your existing homepage view function
def homepage(request):
    return render(request, 'jurrmarketplace/homepage.html')

# New create_assignment view function
@login_required
def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.company = request.user.company
            assignment.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()

    return render(request, 'jurrmarketplace/create_assignment.html', {'form': form})

def assignment_list(request):
    assignments = Assignment.objects.filter(status='Open')
    return render(request, 'jurrmarketplace/assignment_list.html', {'assignments': assignments})

def company_login(request):
    return handle_login(request, 'jurrmarketplace/company_login.html')

def lawyer_login(request):
    return handle_login(request, 'jurrmarketplace/lawyer_login.html')

def handle_login(request, template_name):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, template_name, {'form': form})

def company_register(request):
    return handle_register(request, 'jurrmarketplace/company_register.html')

def lawyer_register(request):
    return handle_register(request, 'jurrmarketplace/lawyer_register.html')

def handle_register(request, template_name):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, template_name, {'form': form})
def apply_for_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)

    if request.method == 'POST':
        form = AssignmentApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.assignment = assignment
            application.lawyer = request.user
            application.save()
            return redirect('assignment_list')  # Redirect to the assignment list after applying

    else:
        form = AssignmentApplicationForm()

    return render(request, 'jurrmarketplace/apply_for_assignment.html', {'form': form, 'assignment': assignment})