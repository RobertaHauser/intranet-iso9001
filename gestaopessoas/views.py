from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import for_reh_001
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin


# Create your views here.
class for_reh_001c(GroupRequiredMixin,CreateView):
    group_required = u"rh1"#somente usuarios do grupo, podem executar [u"rh1",u"sgq1",...]
    model = for_reh_001
    fields = "__all__"
    template_name = 'form.html'
    success_url = reverse_lazy('for_reh_001r')

class for_reh_001r(ListView):
    model = for_reh_001
    template_name = 'for_reh_001r.html'


class for_reh_001u(GroupRequiredMixin, UpdateView):
    group_required = u"rh1"
    model = for_reh_001
    fields = "__all__"
    template_name = 'form.html'
    success_url = reverse_lazy('for_reh_001r')

def for_reh_001d(request,pk):
    #group_required = u"rh1"
    db=for_reh_001.objects.get(pk=pk)
    db.delete()
    return redirect('for_reh_001r')