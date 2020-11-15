from rest_framework import serializers

from core.base_serializer import BaseSerializer


class TokenSerializer(BaseSerializer):
    refresh = serializers.CharField()
    access = serializers.CharField()

    class Meta:
        fields = ('refresh', 'access')
        read_only_fields = ('refresh', 'access')


class UniqueTokenSerializer(BaseSerializer):
    token = serializers.CharField()

    class Meta:
        fields = ('token',)
        read_only_fields = ('token',)
