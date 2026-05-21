from django.urls import path
from complaints import views

urlpatterns = [
    path('terms/', views.terms, name='terms'),
    path('file-complaint/', views.file_complaint, name='file_complaint'),
    path('complaint-success/<int:complaint_id>/', views.complaint_success, name='complaint_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('complaint/<int:complaint_id>/', views.complaint_detail, name='complaint_detail'),
    path('track/', views.track_complaint, name='track_complaint'),
]