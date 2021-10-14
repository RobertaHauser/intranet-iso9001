from django.urls import path
from .views import for_reh_001r

urlpatterns = [
    path('for_reh_001r/', for_reh_001r.as_view(), name='for_reh_001r'),
]