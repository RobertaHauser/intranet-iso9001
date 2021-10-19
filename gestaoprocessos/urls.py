from django.urls import path
from .views import tab_sgq_001r

urlpatterns = [
    path('tab_sgq_001r/', tab_sgq_001r.as_view(), name='tab_sgq_001r'),
]