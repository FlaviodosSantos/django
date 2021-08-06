from django.views import generic
from django.urls import reverse_lazy
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2 #paginação

class PostDetail(generic.DeleteView):
    model = Post
    template_name = 'post_detail.html'

class PostCreate(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('home')
