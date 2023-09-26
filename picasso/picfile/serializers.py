from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'

    def create(self, validated_data):
        if not 'processed':
            newfile = File.objects.create(**validated_data)
            return newfile
