from rest_framework.serializers import ModelSerializer

from APP.models.Test import Test
import json

class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instanse):
        return instanse