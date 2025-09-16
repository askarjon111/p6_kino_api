from django.urls import path
from apps.meta.api_endpoints import watchsession


urlpatterns = [
    path('watch-session-create/',
         watchsession.WatchSessionCreateView.as_view(),
         name='watch_session_create'),
]
