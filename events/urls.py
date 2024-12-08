from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('event_list/', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/update/', views.update_event, name='update_event'),  # URL for event update
    path('event/<int:pk>/delete/', views.delete_event, name='delete_event'),  # URL for event delete
    path('event/<int:pk>/register/', views.register_for_event, name='register_for_event'),  # New URL for event registration
    path('calendar/', views.event_calendar, name='event_calendar'),  # New URL for the calendar
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('creation-success/', views.creation_success, name='creation_success'),
    path('admin/', views.create_event, name='admin'),  
    path('create-category/', views.create_category, name='create_category'),  
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

