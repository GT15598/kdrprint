from django.shortcuts import render, get_object_or_404
from .models import Project
from .models import Project, Service
from django.contrib import messages    

def home(request):
    featured_projects = Project.objects.filter(
        is_featured=True
    ).order_by('-created_at')[:4]

    return render(
        request,
        'main/home.html',
        {
            'featured_projects': featured_projects,
        }
    )


def services(request):
    services_list = Service.objects.filter(
        is_active=True
    ).order_by('number', 'created_at')

    return render(
        request,
        'main/services.html',
        {
            'services': services_list,
        }
    )

def service_detail(request, slug):
    service = get_object_or_404(
        Service.objects.prefetch_related('gallery'),
        slug=slug,
        is_active=True
    )

    related_services = Service.objects.filter(
        is_active=True
    ).exclude(
        id=service.id
    ).order_by('number')[:3]

    return render(
        request,
        'main/service_detail.html',
        {
            'service': service,
            'related_services': related_services,
        }
    )

def portfolio(request):
    projects = Project.objects.all().order_by('-created_at')

    return render(
        request,
        'main/portfolio.html',
        {
            'projects': projects,
        }
    )


def project_detail(request, project_id):
    project = get_object_or_404(
        Project,
        id=project_id
    )

    return render(
        request,
        'main/project_detail.html',
        {
            'project': project,
        }
    )


def about(request):
    return render(request, 'main/about.html')

def contacts(request):

    if request.method == 'POST':

        ContactRequest.objects.create(
            name=request.POST.get('name', '').strip(),
            phone=request.POST.get('phone', '').strip(),
            email=request.POST.get('email', '').strip(),
            message=request.POST.get('message', '').strip(),
        )

        return redirect('contacts')

    return render(
        request,
        'main/contacts.html'
    )


