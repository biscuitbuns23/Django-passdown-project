from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('UserBase/', include('UserBase.urls', namespace='userbase')),
    path('Menu/', include('Menu.urls', namespace='menu')),
    path('__reload__/', include('django_browser_reload.urls')),
]
