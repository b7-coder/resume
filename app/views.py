from django.shortcuts import render
from .models import *
from django.shortcuts import HttpResponse
import os

def index(request):
    educations = Education.objects.all()
    experiences = Experience.objects.all()

    context = {
        'educations':educations,
        'experiences':experiences
    }

    return render(request, 'index.html', context)

def blog(request):
    blogs = Blog.objects.all()
    context = { 'blogs': blogs }
    return render(request, 'blog.html', context)

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        row = Applications.objects.create(name = name, email = email, message=message)
        row.save()

    return render(request, 'contact.html')

def portfolio(request):
    projects = Projects.objects.all()

    context = {
        'projects':projects
    }

    return render(request, 'portfolio.html', context)

def resume(request):
    educations = Education.objects.all()
    experiences = Experience.objects.all()

    context = {
        'educations':educations,
        'experiences':experiences
    }

    return render(request, 'resume.html', context)

def download_resume(request):
    file_path = os.path.join('static', 'resume.txt')
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
    return response

def blogDetails(request, id):
    row = Blog.objects.get(id=id)
    rows = BlogDetails.objects.filter(blogObject=row)
    comments = Comments.objects.filter(blogObject=row)

    context = {
        'row':row,
        'rows':rows,
        'comments':comments
    }

    return render(request, 'blog-detail.html', context)

def comments(request, id):

    if request.method == 'POST':
        user = request.POST.get('user')
        message = request.POST.get('message')

        blog = Blog.objects.get(id=id)

        row = Comments.objects.create(user = user, message=message, blogObject=blog)
        row.save()

    return blogDetails(request, id)