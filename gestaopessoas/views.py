from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import for_reh_001
from django.urls import reverse_lazy


# Create your views here.
class for_reh_001c(CreateView):
    #group_required = u"rh1"#somente usuarios do grupo, podem executar
    model = for_reh_001
    fields = "__all__"
    template_name = 'form.html'
    success_url = reverse_lazy('for_reh_001r')

class for_reh_001r(ListView):
    model = for_reh_001
    template_name = 'for_reh_001r.html'


class for_reh_001u(UpdateView):
    #group_required = u"rh1"
    model = for_reh_001
    fields = "__all__"
    template_name = 'form.html'
    success_url = reverse_lazy('for_reh_001r')