from django.shortcuts import render, HttpResponse

from main.models import Article


# Create your views here.
def index(request):
    return render(request, "main.html", {"articles": Article.objects.all()})
