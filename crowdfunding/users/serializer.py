from rest_framework import serializers
from .models import CustomUser
from projects.serializers import ProjectSerializer, PledgeSerializer

class CustomUserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    

class CustomUserDetailSerializer (CustomUserSerializer):

    supported_pledges = PledgeSerializer(many=True, read_only=True)
    owned_projects = ProjectSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance   