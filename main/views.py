from django.shortcuts import render, HttpResponse

from main.models import Tags
from main.models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all().prefetch_related('tags_set')
    return render(request, 'main.html', {'articles': articles})