from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

from .forms import PostForm
from .models import Category, Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'cats/create.html'

    def get_success_url(self):
        return reverse(
            'cat:home'
        )


def categories(request):
    categories = Category.objects.filter(
        is_published=True
    )
    context = {'categories': categories}
    return render(request, 'cats/categories.html', context)
