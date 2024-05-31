from django.shortcuts import render, redirect
from .models import Post_model
# Create your views here.

def home(request):
    all_data = Post_model.objects.all()
    content = {'blogs':all_data} 
    return render (request,'index.html', context=content)
    
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        created_date = request.POST.get('created_at')
        Post_model.objects.create(title=title, content=content, author=author, created_date=created_date)
        return redirect('home')
    return render (request,'create.html')