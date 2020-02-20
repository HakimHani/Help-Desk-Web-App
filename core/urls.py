from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.api import MessageModelViewSet, UserModelViewSet

router = routers.SimpleRouter()
router.register(r'message', MessageModelViewSet)
router.register(r'user', UserModelViewSet)

urlpatterns = [
    path(r'api/v1/', include(router.urls)),

    path('', login_required(
        TemplateView.as_view(template_name='core/chat.html')), name='home'),
]
