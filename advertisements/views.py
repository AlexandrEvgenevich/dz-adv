from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwner
from django_filters import rest_framework


class AdvertisementFilter(rest_framework.FilterSet):
    filter_date = rest_framework.DateFromToRangeFilter()
    filter_status = rest_framework.CharFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    model = Advertisement
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['creator', 'status', 'created_at']
    filterset_class = AdvertisementFilter
    search_fields = ['creator', 'status', 'created_at']
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.request.method == 'GET':
            return []
        return [IsAuthenticatedOrReadOnly(), IsOwner()]
