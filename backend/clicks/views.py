from rest_framework import response
from rest_framework import status
from rest_framework import views

from clicks import models
from clicks.services import clicks as clicks_service
from clicks import serializers


def _get_client_ip(request):
    """
    Gets client ip from the request

    On Heroku, the client's IP is guaranteed to be the first address in X_FORWARDED_FOR, but
    we fall back to REMOTE_ADDR just in case.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ips = x_forwarded_for.split(',')
    else:
        ips = [request.META.get('REMOTE_ADDR')]
    return [ip.strip() for ip in ips][0]


class ClicksList(views.APIView):
    def get(self, request, format=None, status=status.HTTP_200_OK):
        click_data = clicks_service.get_click_data()
        serializer = serializers.ClickDataForParty(click_data, many=True)
        return response.Response(serializer.data, status=status)

    def post(self, request, format=None):
        serializer = serializers.ClickRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ip_address = _get_client_ip(request)

        clicks_service.add_click_record(
            party_id=serializer.validated_data.get('id'),
            clicks=serializer.validated_data.get('clicks'),
            ip_address=ip_address,
        )

        return self.get(request, status=status.HTTP_201_CREATED)


class PartyList(views.APIView):
    def get(self, request, format=None):
        parties = models.Party.objects.all()
        serializer = serializers.PartySerializer(parties, many=True)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
