from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .forms import PostForm
from .models import Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'cats/create.html'

    def get_success_url(self):
        return reverse(
            'cat:home'
        )
