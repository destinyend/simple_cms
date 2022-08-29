from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import include, path
from main import views
from django.conf.urls.static import static
from simple_cms import settings

router = DefaultRouter()
for name in views.__dict__:
    if name.endswith('View') and name not in ('APIView', 'ViewSet', 'TokenObtainPairView', 'GenericAPIView'):
        url = name.replace('View', '').lower()
        router.register(url, getattr(views, name), basename=url)


urlpatterns = [
    path('', include(router.urls)),
    path('token_obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
