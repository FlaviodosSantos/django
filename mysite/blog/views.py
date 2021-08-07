from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2 #paginação

class PostDetail(generic.DeleteView):
    model = Post
    template_name = 'post_detail.html'

@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class PostCreate(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('home')

@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class PostUpdate(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('home')

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

