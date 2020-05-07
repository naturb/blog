from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'web/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'web/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # newest on top

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'web/about.html', {'title':'About'})

def register(request):
   return render(request, 'users/register.html', context)