from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    # write_only 사용해서 사용자에게 넘어가지 않도록 설정 (오버라이드)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        # confirm은 쓰지 않는다. 시리얼라이즈 하는게 아닌 확인 작업이기에..
        fields = ('username', 'password')