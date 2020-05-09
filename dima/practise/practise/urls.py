from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('exit/', authViews.LogoutView.as_view(), name='exit_a'),
    path('', include('personal_area.urls')),
]
