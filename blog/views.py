from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *

def posts(request):
    post = Post.objects.all().order_by('-date')
    form = PostForm()
    paginator = Paginator(post, 10)
    page = request.GET.get('page')
    try:
        info = paginator.page(page)
    except PageNotAnInteger:
        info = paginator.page(1)
    except EmptyPage:
        info = paginator.page(paginator.num_pages)
    if page == '1':
        return redirect('/', permanent=True)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post (
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
            ).save()
            return redirect('/')

    return render(request, 'blog/blog_list.html', {'posts': info, 'form':form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


