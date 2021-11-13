from . import models
from django.shortcuts import redirect, render
from .constants import *
from django.contrib.auth import authenticate, login, logout

def logo(request):
    logout(request)
    return redirect('onboarding:login')

def logi(request):
    if request.method == 'POST':
        print("Post")
        username = request.POST.get('username').title()
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('onboarding:dashboard')
        else:
            print("Invalid Credentials")
            return render(request, LOGIN_HTML, {'err': 'Invalid Credentials'})
    return render(request, LOGIN_HTML)

def dashboard(request):
    group = getattr(models, 'user_group').objects.filter(**{'user__username': str(request.user)}).values_list('group__name', flat=True)[0]
    if group == 'Recruiter':
        pending = getattr( models, 'candidate').objects.filter(**{'created_by': str(request.user), 'status': 'Pending'}).order_by('created_datetime').count()
        approved = getattr( models, 'candidate').objects.filter(**{'created_by': str(request.user), 'status': 'Approved'}).order_by('created_datetime').count()
    elif group == 'Obspoc':
        pending = getattr( models, 'candidate').objects.filter(**{'obspoc': str(request.user), 'status': 'Pending'}).order_by('created_datetime').count()
        approved = getattr( models, 'candidate').objects.filter(**{'obspoc': str(request.user), 'status': 'Approved'}).order_by('created_datetime').count()
    else:
        pending = getattr( models, 'candidate').objects.filter(**{'status': 'Pending'}).order_by('created_datetime').count()
        approved = getattr( models, 'candidate').objects.filter(**{'status': 'Approved'}).order_by('created_datetime').count()

    return render(request, DASHBOARD_CONTAINER_HTML, {'group': group, 'pending': pending, 'approved': approved})

def create_candidate(request):
    if request.method == 'POST':
        save_map = {
            'first_name': request.POST.get('firstname'),
            'middle_name': request.POST.get('middlename'),
            'last_name':request.POST.get('lastname'),
            'dob':request.POST.get('dob'),
            'phone':request.POST.get('phone'),
            'adhaar':request.POST.get('adhaar'),
            'doj':request.POST.get('doj'),
            'fk_function_id':request.POST.get('function'),
            'fk_sub_function_id':request.POST.get('subfunction'),
            'fk_designation_id':request.POST.get('designation'),
            'fk_state_id':request.POST.get('state'),
            'fk_location_id':request.POST.get('location'),
            'fk_sub_location_id':request.POST.get('sublocation'),
            'created_by':str(request.user),
            'recruiter':request.POST.get('recruiter'),
            'obspoc':request.POST.get('obspoc'),
            'status':'Pending'
        }
        getattr(models, 'candidate').objects.create(**save_map)
        msg = 'Candidate created successfully'
        all_candidate = getattr( models, 'candidate').objects.filter(**{'created_by': str(request.user)}).order_by('created_datetime')
        return render(request, CANDIDATE_TABLE_CONTAINER_HTML, {'data': all_candidate})
    context = {
        'function' : getattr(models, 'function').objects.all(),
        'subfunction' : getattr(models, 'sub_function').objects.all(),
        'designation' : getattr(models, 'designation').objects.all(),
        'state' : getattr(models, 'state').objects.all(),
        'location' : getattr(models, 'location').objects.all(),
        'sublocation' : getattr(models, 'sub_location').objects.all(),
        'recruiters': getattr(models, 'user_group').objects.filter(**{'group__name': 'Recruiter'}),
        'obspocs': getattr(models, 'user_group').objects.filter(**{'group__name': 'Obspoc'})
    }
    return render(request, CANDIDATE_CRUD_CONTAINER_HTML, context)

def update_candidate(request, cid):
    if request.method == 'POST':
        save_map = {
            'status':'Pending'
        }
        getattr(models, 'candidate').objects.filter(**{'pk': cid}).update(**save_map)
        msg = 'Candidate updated successfully'
        all_candidate = getattr( models, 'candidate').objects.filter(**{'created_by': str(request.user)}).order_by('created_datetime')
        return render(request, CANDIDATE_TABLE_CONTAINER_HTML, {'data': all_candidate})
    selected = getattr(models, 'candidate').objects.get(**{'id': cid})
    return render(request, CANDIDATE_EDIT_CONTAINER_HTML, {'selected': selected})

def view_candidate(request, cid):    
    selected = getattr(models, 'candidate').objects.get(**{'id': cid})
    return render(request, CANDIDATE_VIEW_CONTAINER_HTML, {'selected': selected})

def all_candidate(request):
    group = getattr(models, 'user_group').objects.filter(**{'user__username': str(request.user)}).values_list('group__name', flat=True)[0]
    if group == 'Recruiter':
        all_candidate = getattr( models, 'candidate').objects.filter(**{'created_by': str(request.user)}).order_by('created_datetime')
    elif group == 'Obspoc':
        all_candidate = getattr( models, 'candidate').objects.filter(**{'obspoc': str(request.user)}).order_by('created_datetime')
    else:
        all_candidate = getattr( models, 'candidate').objects.all().order_by('created_datetime')
    return render(request, CANDIDATE_TABLE_CONTAINER_HTML, {'data': all_candidate})