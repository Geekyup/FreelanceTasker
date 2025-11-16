from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjectForm
from .models import Project

def index(request):
    return render(request, 'main/index.html')

def main(request):
    return render(request, 'main/main.html')

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'main/main.html', {'form': form})

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('projects')

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/main.html', {'form': form})

def profile(request):
    return render(request, 'main/profile.html')