from rest_framework import serializers

from clicks import models


class ClickRecordSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    clicks = serializers.IntegerField()


class ClickDataForParty(serializers.Serializer):
    id = serializers.IntegerField()
    rate = serializers.FloatField()
    ten_minutes = serializers.IntegerField()
    one_hour = serializers.IntegerField()
    one_day = serializers.IntegerField()
    all_time = serializers.IntegerField()


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Party
        fields = (
            'id',
            'name',
            'primary_color',
            'secondary_color',
            'image',
        )
