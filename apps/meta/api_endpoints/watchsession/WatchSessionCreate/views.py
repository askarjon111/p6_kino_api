from rest_framework.views import APIView
from rest_framework.response import Response

from apps.meta.api_endpoints.watchsession.WatchSessionCreate.serializers import WatchSessionCreateSerializer


class WatchSessionCreateView(APIView):
    def post(self, request):
        serializer = WatchSessionCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({'status': 'ok'})
