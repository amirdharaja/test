from rest_framework.viewsets import ModelViewSet

from APP.models.Test import Test
from APP.serializers import (
    TestSerializer
)


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer