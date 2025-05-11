from django.shortcuts import render, redirect

from article.models import Article


def index(request):
    articles = Article.objects.all()

    return render(request, 'index.html', { 'articles': articles })


def show(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request, 'show.html', { 'article': article })


def create(request):
    if request.method == 'POST':
        article = Article()
        article.author = request.user
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('article:show', pk=article.id)
    else:
        return render(request, 'new.html')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('article:show', pk=article.id)
    else:
        return render(request, 'edit.html', { 'article': article })


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article:index')