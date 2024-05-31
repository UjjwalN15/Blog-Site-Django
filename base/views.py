from django.shortcuts import render, redirect
from .models import Post_model
# Create your views here.

def home(request):
    all_data = Post_model.objects.all()
    content = {'blogs':all_data} 
    return render (request,'index.html', context=content)
def edit(request, pk):
    blog = Post_model.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        created_date = request.POST.get('created_at')
        #Line number 20 ko todo object of Todo_Table
        blog.title = title
        blog.content = content
        blog.author = author
        blog.created_date = created_date
        blog.save()
        return redirect('home')
    edit_blog = {'blog' : blog}
    return render(request,'edit.html', context=edit_blog)

def view(request, pk):
    blog = Post_model.objects.get(id=pk)
    edit_blog = {'blog' : blog}
    return render(request,'view.html', context=edit_blog)
    
def delete(request, pk):
    blog = Post_model.objects.get(id=pk)
    blog.delete()
    return redirect('home')


def Admin(request):
    return render(request, 'admin', context={"current_url": "admin"})
    
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        created_date = request.POST.get('created_at')
        Post_model.objects.create(title=title, content=content, author=author, created_date=created_date)
        return redirect('home')
    return render (request,'create.html', context={"current_url": "create"})

def delete_all(request):
    blog = Post_model.objects.all()
    blog.delete()
    return redirect ('home')