from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post
from django.urls import reverse


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = [ "title", "subtitle", "body"]
    
    def get_success_url(self):
        return reverse('list')
