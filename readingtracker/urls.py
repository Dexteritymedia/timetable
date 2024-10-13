from django.urls import path
from .views import upload_file, reading_session, summary

app_name = 'tracker'

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('reading_session/<int:session_id>/', reading_session, name='reading_session'),
    path('summary/<int:session_id>/', summary, name='summary'),
]
