from django.views.generic.list import ListView
from .models import for_reh_001

# Create your views here.
class for_reh_001r(ListView):
    model = for_reh_001
    template_name = 'for_reh_001r.html'