from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('projects',views.project,name='project'),
    path('blogs',views.blog,name='blog'),
    path('experience',views.exp,name='exp'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
