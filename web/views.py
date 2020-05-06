from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Natalia',
        'title': 'The first blog post',
        'content': 'First post content',
        'date_posted': 'May 1, 2020'
    },
    {
        'author': 'Anne Marie',
        'title': 'The second blog post',
        'content': 'Second post content',
        'date_posted': 'May 2, 2020'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'web/home.html', context)

def about(request):
    return render(request, 'web/about.html', {'title':'About'})