from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from apps.reports import views

from .views import register_view

docs_urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

auth_urlpatterns = [
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", register_view),
]

api_router = SimpleRouter()
api_router.register(r"groups", views.GroupViewSet, basename="group")
api_router.register(r"students", views.StudentViewSet, basename="student")
api_router.register(r"subjects", views.SubjectViewSet, basename="subject")
api_router.register(r"grades", views.GradeViewSet, basename="grade")

urlpatterns = [
    path("auth/", include(auth_urlpatterns)),
    path("docs/", include(docs_urlpatterns)),
    path("", include(api_router.urls)),
]
