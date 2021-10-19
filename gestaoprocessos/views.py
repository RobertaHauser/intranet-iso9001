from django.views.generic.list import ListView
from .models import tab_sgq_001


# Create your views here.
class tab_sgq_001r(ListView):
    model = tab_sgq_001
    template_name = 'tab_sgq_001r.html'
