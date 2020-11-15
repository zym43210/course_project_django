from rest_framework import serializers

from core.base_serializer import BaseSerializer


class DecodeSerializer(BaseSerializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField()
    exp = serializers.IntegerField()
    email = serializers.CharField()

    class Meta:
        fields = ('user_id', 'username', 'exp', 'email',)
        read_only_fields = ('user_id', 'username', 'exp', 'email',)
