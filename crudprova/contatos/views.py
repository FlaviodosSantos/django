
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contatos

# Create your views here.
class ContatosList(ListView):
    model = Contatos
    paginate_by = 10

class ContatosCreate(CreateView):
    model = Contatos
    fields = "__all__"
    success_url = reverse_lazy('contatos_list')

class ContatosUpdate(UpdateView):
    model = Contatos
    fields = "__all__"
    success_url = reverse_lazy('contatos_list')

class ContatosDelete(DeleteView):
    model = Contatos
    success_url = reverse_lazy('contatos_list')
