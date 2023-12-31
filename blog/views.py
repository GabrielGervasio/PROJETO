from django.shortcuts import render
from django.utils import timezone
from .models import Post, Equipe, Palestra,Atletica
from django.shortcuts import render, get_object_or_404,redirect
from .forms import PostForm



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def equipes(request):
    equipes = Equipe.objects.all()
    return render(request, 'blog/equipes.html', {'equipes': equipes})

def equipe_detail(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    return render(request, 'blog/equipe_detail.html', {'equipe': equipe})

def palestra(request):
    palestra = Palestra.objects.all()
    return render(request, 'blog/palestra.html', {'palestra': palestra})

def atletica(request):
    atletica = Atletica.objects.all()
    return render(request, 'blog/atletica.html', {'atletica': atletica})

def detalhes_atletica(request, atletica_id):
    atletica = Atletica.objects.get(pk=atletica_id)
    return render(request, 'blog/detalhes_atletica.html', {'atletica': atletica})

def projeto(request):
    return render(request, 'blog/projeto.html', {'projeto': projeto})


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
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})