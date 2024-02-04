from rest_framework import serializers
from .models import User, Step


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'
