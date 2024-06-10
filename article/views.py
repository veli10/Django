from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm

# Create your views here.
def home__view(request):
    articles = Article.objects.all()
    return render(request,'index.html', {'articles': articles})

@login_required(login_url='account:login')
def articles__view(request):
    search_query = request.GET.get('search')
    
    if search_query:
        articles = Article.objects.filter(title__contains=search_query)
        return render(request,'articles.html', {'articles': articles})

    articles = Article.objects.all()
    return render(request,'articles.html', {'articles': articles})

@login_required(login_url='account:login')
def addarticles__view(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, 'Article created successfuly')
        return redirect('dashboard')

    context = {'form': form}
    return render(request,'addarticles.html', context)

@login_required(login_url='account:login')
def article__update__view(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, 'Article created successfuly')
        return redirect('dashboard')

    context = {'form': form}
    return render(request,'update-article.html', context)

@login_required(login_url='account:login')
def article__delete__view(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, 'Article created successfuly')
    return redirect('dashboard')



@login_required(login_url='account:login')
def article_detail_view(request, id):
    article = get_object_or_404(Article, id = id)
    comments = Comment.objects.filter(article = article)
    
    context = {
        "article": article,
        "comments": comments,
    }
    return render(request,'article-detail.html', context)

def dashboard__view(request):
    articles = Article.objects.filter(author = request.user)
    return render(request,'dashboard.html', {'articles': articles})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

@login_required(login_url='account:login')
def addcomment__view(request, id):
    article = get_object_or_404(Article, id = id)

    if request.method == 'POST':
        comment_author = request.POST.get('comment__author')
        comment_content = request.POST.get('comment__content')

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article = article
        newComment.save()
        return redirect(reverse('article-detail', kwargs={'id': id}))
