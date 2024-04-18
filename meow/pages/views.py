from random import randint

from django.shortcuts import render

from cats.models import Post


def home_page(request):
    number_of_posts = Post.objects.count()
    random_number = randint(1, number_of_posts)
    random_post = Post.objects.get(id=random_number)
    context = {'post': random_post}
    return render(request, 'cats/cats.html', context)
