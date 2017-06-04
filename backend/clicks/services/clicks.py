from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone
from rest_framework import exceptions

from clicks import models


refresh_rate = 1


def _get_party(id):
    try:
        return models.Party.objects.get(id=id)
    except models.Party.DoesNotExist:
        raise exceptions.NotFound()


def _get_click_rate_for_party(party):
    clicks = party.clicks.filter(
        created_time__gt=timezone.now() - timedelta(seconds=refresh_rate),
    ).aggregate(clicks=Sum('clicks'))['clicks'] or 0

    return clicks / refresh_rate


def get_click_data():
    time_periods = {
        # Hack, I know
        'all_time': timezone.now() - timedelta(days=10000),
        'ten_minutes': timezone.now() - timedelta(seconds=5),
        'one_hour': timezone.now() - timedelta(seconds=10),
        'one_day': timezone.now() - timedelta(minutes=1),
    }

    click_data_for_party = {party.id: {
        'id': party.id,
        'rate': _get_click_rate_for_party(party),
        'ten_minutes': 0,
        'one_hour': 0,
        'one_day': 0,
        'all_time': 0,
    } for party in models.Party.objects.all()}

    for time_name, delta in time_periods.items():
        parties = models.Party.objects.filter(
            clicks__created_time__gt=delta,
        ).annotate(
            clicks_in_window=Sum('clicks__clicks')
        )

        for party in parties:
            click_data_for_party[party.id][time_name] = party.clicks_in_window

    return click_data_for_party.values()


def add_click_record(party_id, clicks, ip_address):
    party = _get_party(party_id)

    models.ClickRecord.objects.create(
        party=party,
        clicks=clicks,
        ip_address=ip_address,
    )
