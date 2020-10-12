from rest_framework.response import Response
from rest_framework.decorators import permission_classes, APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_200_OK as ok,
    HTTP_201_CREATED as created,
    HTTP_202_ACCEPTED as accepted,
    HTTP_400_BAD_REQUEST as bad_request,
    HTTP_401_UNAUTHORIZED as un_authorized,
    HTTP_403_FORBIDDEN as forbidden,
    HTTP_404_NOT_FOUND as not_found,
    HTTP_405_METHOD_NOT_ALLOWED as method_not_allowed,
)

from APP.helpers import validate
from APP.models.Test import Test
from APP.serializers import (
    TestSerializer,
)


@permission_classes((AllowAny,))
class Home(APIView):

    def get(self, request):
        test_data = Test.objects.all()
        test_data = TestSerializer(test_data,  many=True)
        return Response({'status': True, 'test_data': test_data.data, }, status=ok)

    def post(self, request):
        list_data = request.data.get('list')
        key = request.data.get('key')

        is_valid = validate(list_data, key)
        if not is_valid['status']:
            return Response(is_valid, status=bad_request)

        key, temp, outputs, output_length, output_total = int(key), [], [], len(list_data), 0
        for d in list_data:
            if d >= key:
                temp = []
                temp.append(d)
                new = {
                    'testdata': str(list_data),
                    'result': str(temp)
                }
                serializer = TestSerializer(data=new)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'status': True, 'Sub Array': temp}, status=ok)
            else:
                temp.append(int(d))
                output_total += d
                if output_total >= key and len(temp) < output_length:
                    output_length = len(temp)
                    outputs = temp.copy()
                    temp = []
                    output_total = 0

        new = {
            'testdata': str(list_data),
            'result': str(temp)
        }
        serializer = TestSerializer(data=new)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': True, 'Sub Array': outputs }, status=ok)