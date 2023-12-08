from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mkchat/', include('mkchat.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]
admin.site.site_header = 'адміністрація'
