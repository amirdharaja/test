from rest_framework.response import Response
from rest_framework.decorators import permission_classes, APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_200_OK as ok,
    HTTP_201_CREATED as created,
    HTTP_400_BAD_REQUEST as bad_request,
    HTTP_404_NOT_FOUND as not_found,
)

from APP.models.Test import Test
from APP.serializers import (
    TestSerializer,
)
import json

@permission_classes((AllowAny,))
class Home(APIView):

    def get(self, request):
        test_data = Test.objects.all()
        test_data = TestSerializer(test_data, many=True)
        data = []
        for d in test_data.data:
            d = (d.testdata).replace("'", '"')
            d = json.loads(d)
            data.append(d)
        if not data:
            return Response({'status': False, 'detail': 'NO DATA FOUND'}, status=not_found)

        return Response({'status': True, 'test data': data}, status=ok)

    def post(self, request):
        test_data = request.data.get('test_data')

        if not test_data or not type(test_data) == dict:
            return Response({'status': False, 'detail': 'PLEASE GIVE VALID INPUT FORMAT(PYTHON DICTONARY)'}, status=bad_request)

        new = { 'testdata': str(test_data),}
        serializer = TestSerializer(data=new)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': True, 'detail': 'DICTONARY ACCEPTED AND SAVED INTO DATABASE' ,'data': test_data }, status=created)