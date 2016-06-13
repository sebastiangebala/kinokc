from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def repertuar(request):
	posts = Post.objects.all().order_by('display_date', 'godzina')
	return render(request, 'kinokc/repertuar.html', {'posts': posts})
def start(request):
    return render(request, 'kinokc/start.html', {'start': start})
def bilety(request):
    return render(request, 'kinokc/bilety.html', {'bilety': bilety})
def rezerwacje(request):
    return render(request, 'kinokc/rezerwacje.html', {'rezerwacje': rezerwacje})
def partnerzy(request):
    return render(request, 'kinokc/partnerzy.html', {'partnerzy': partnerzy})
def kontakt(request):
    return render(request, 'kinokc/kontakt.html', {'kontakt': kontakt})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'kinokc/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'kinokc/post_new.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'kinokc/post_new.html', {'form': form})
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('kinokc.views.repertuar')
