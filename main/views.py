from django.shortcuts import get_object_or_404, render

from .models import Project, BlogPost


def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def blog_ls(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})