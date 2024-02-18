from django.shortcuts import render
from .models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.order_by('-published_at')
    tags = Tag.objects.all()

    tag_id = request.GET.get('tag')
    if tag_id:
        object_list = object_list.filter(tags__id=tag_id)

    context = {'object_list': object_list, 'tags': tags}

    return render(request, template, context)
