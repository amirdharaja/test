from rest_framework.serializers import ModelSerializer

from APP.models.Test import Test
import json

class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instanse):
        test_data = super().to_representation(instanse)
        d = (test_data['testdata']).replace("'", '"')
        d = json.loads(d)
        data = {'id':test_data['id'], 'test_data': d}
        return data