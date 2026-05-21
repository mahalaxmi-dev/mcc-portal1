from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', user_views.home, name='home'),

    path('register/', user_views.register, name='register'),
    path('register/success/', user_views.register_success, name='register_success'),

    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout_view, name='logout'),

    path('forgot-username/', user_views.forgot_username, name='forgot_username'),
    path('forgot-password/', user_views.forgot_password, name='forgot_password'),

    path('about/', user_views.about, name='about'),
    path('faqs/', user_views.faqs, name='faqs'),

    path('officers-directory/', user_views.officers_directory, name='officers_directory'),

    path('complaints/', include('complaints.urls')),

    path('officer/', include('officers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)