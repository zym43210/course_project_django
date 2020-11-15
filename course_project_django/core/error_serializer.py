from rest_framework import serializers

from core.base_serializer import BaseSerializer


class ErrorSerializer(BaseSerializer):
    error = serializers.CharField(required=True)
    error_code = serializers.IntegerField(required=False)

    class Meta:
        fields = ('error', 'error_code')
        read_only_fields = ('error', 'error_code')


class StandartErrorSerializer(BaseSerializer):
    detail = serializers.CharField()

    class Meta:
        fields = ('detail',)
        read_only_fields = ('detail',)
