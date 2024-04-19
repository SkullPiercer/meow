from random import choice

from django.shortcuts import render

from cats.models import Post


def home_page(request):
    random_post = choice(Post.objects.all())
    context = {'post': random_post}
    return render(request, 'cats/cats.html', context)
