from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import RegisterSerializer


@extend_schema(request=RegisterSerializer, responses=RegisterSerializer)
@api_view(http_method_names=["POST"])
@permission_classes((AllowAny,))
def register_view(request: Request) -> Response:
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
