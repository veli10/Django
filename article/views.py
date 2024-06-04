from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.
def home__view(request):
    articles = Article.objects.all()
    return render(request,'index.html', {'articles': articles})

@login_required(login_url='account:login')
def articles__view(request):
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
    context = {'article': article}
    return render(request,'article-detail.html', context)

def dashboard__view(request):
    articles = Article.objects.filter(author = request.user)
    return render(request,'dashboard.html', {'articles': articles})

def custom_404(request, exception):
    return render(request, '404.html', status=404)