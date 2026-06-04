from django.shortcuts import render,get_object_or_404
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


def category(request):
    category=Category.objects.all()
    posts = Post.objects.all()
    context = {'posts': posts, 'category': category,}

    return render(request,'categories.html',context)

def post_category(request,id):
    category_id = get_object_or_404(Category,id=id)
    posts=Post.objects.filter(category_id=category_id)
    context={'posts':posts,'category_id':category_id}

    return render(request,'posts_by_categories.html',context)


def about(request):
    return render(request,'about.html')

def post_detail(request,slug):

    post=get_object_or_404(Post,slug=slug)


    context = {'post':post}
    return render(request,'post-detail.html',context)