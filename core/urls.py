# from django.conf.urls.static import static
# from django.conf import settings
# from app.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllTasks.as_view(), name='all_tasks'),
    path('important/', views.ImportantTasks.as_view(), name='important_tasks'),
    path('completed/', views.CompletedTasks.as_view(), name='completed_tasks'),
    path('simple_list_view/', views.SimpleListView.as_view(), name='all_tasks_listed'),
    path('task/<int:pk>/', views.SimpleDetailView.as_view(), name='task_detailed'), #http://127.0.0.1:8000/task/6/
    path('simple_redirect_view/', views.SimpleRedirectView.as_view(), name='redirect'),
    path('simple_form_view/', views.SimpleFormView.as_view(), name='form'),
]

# if settings.DEBUG:
#     urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)