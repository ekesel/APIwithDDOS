from rest_framework import serializers

class loginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100)

class FileSerializer(serializers.Serializer):
    files = serializers.FileField()