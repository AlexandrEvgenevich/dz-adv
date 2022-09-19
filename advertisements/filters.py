from django_filters.rest_framework import FilterSet
from django_filters import DateTimeFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""

    created_at = DateTimeFromToRangeFilter()

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['creator', 'status']
