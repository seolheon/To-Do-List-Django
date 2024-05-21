# from django.conf.urls.static import static
# from django.conf import settings
# from prodcostcalc.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllTasks.as_view(), name='all_tasks'),
    path('important/', views.ImportantTasks.as_view(), name='important_tasks'),
    path('completed/', views.CompletedTasks.as_view(), name='completed_tasks'),
]

# if settings.DEBUG:
#     urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)