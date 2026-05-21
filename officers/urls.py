from django.urls import path
from officers import views

urlpatterns = [
    path('login/', views.officer_login, name='officer_login'),
    path('dashboard/', views.officer_dashboard, name='officer_dashboard'),
    path('complaint/<int:complaint_id>/', views.officer_complaint_detail, name='officer_complaint_detail'),
    path('logout/', views.officer_logout, name='officer_logout'),
]