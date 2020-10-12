from rest_framework.serializers import ModelSerializer

from APP.models.Test import Test


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'testdata', 'result')