from rest_framework import serializers

from core.base_serializer import BaseSerializer


class SuccessSerializer(BaseSerializer):
    success = serializers.BooleanField(initial=True)

    class Meta:
        fields = ('success',)
        read_only_fields = ('success',)
