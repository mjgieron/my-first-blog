from django.utils import timezone
from .models import Post
from .forms import PostForm
from .models import About
from .forms import AboutForm
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.picture = request.POST['picture']
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk).delete()
    return redirect('post_list')

def about_show(request):
    about = get_object_or_404(About)
    return render(request, 'blog/about_show.html', {'about': about})

def about_edit(request, pk):
    about = get_object_or_404(About, pk=pk)
    if request.method == "ABOUT":
        form = AboutForm(request.ABOUT, instance=about)
        if form.is_valid():
            about = form.save(commit=False)
            about.picture = request.ABOUT['picture']
            about.save()
            return redirect('blog/about_show.html')
    else:
        form = AboutForm(instance=about)
    return render(request, 'blog/about_edit.html', {'form': form})
