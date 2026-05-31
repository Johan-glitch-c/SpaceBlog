from django.shortcuts import render
from .models import Post, Category


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context={
        'posts':posts,
    }
    return render(request, 'index.html',context)


def post(request):

    category_id = request.GET.get('category')

    posts = Post.objects.all()

    if category_id:
        posts = posts.filter(category_id=category_id)

    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'active_category': category_id
    }

    return render(request, 'posts.html', context)