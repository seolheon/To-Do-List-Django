# from django.conf.urls.static import static
# from django.conf import settings
# from prodcostcalc.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tasks, name='all_tasks'),
    path('important/', views.important_tasks, name='important_tasks'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
]

# if settings.DEBUG:
#     urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)