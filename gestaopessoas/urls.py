from django.urls import path
from .views import for_reh_001c, for_reh_001r, for_reh_001u, for_reh_001d

urlpatterns = [
    path('for_reh_001c/', for_reh_001c.as_view(), name='for_reh_001c'),
    path('for_reh_001r/', for_reh_001r.as_view(), name='for_reh_001r'),
    path('for_reh_001u/<int:pk>', for_reh_001u.as_view(), name='for_reh_001u'),
    path('for_reh_001d/<int:pk>', for_reh_001d, name='for_reh_001d'),
]