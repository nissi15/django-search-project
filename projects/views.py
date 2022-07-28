# from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source built by the community'
    }
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}

    return render(request, 'projects/projects.html', context)


def project(request, pk): 
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    print('projectobj:', projectobj)
    return render(request, 'projects/single-project.html', {'project': projectobj, 'tags': tags})
   

