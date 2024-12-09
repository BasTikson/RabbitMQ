from rest_framework import serializers
from .models import AboutUs, RequestLog


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['title', 'description', 'created_at']


class RequestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLog
        fields = ['url', 'method', 'ip_address', 'user_agent', 'random_message', 'timestamp']
