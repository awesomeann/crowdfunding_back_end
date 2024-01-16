from rest_framework import serializers
from .models import Project, Pledge


class ProjectSerializer (serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class PledgeSerializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = Project
        fields = '__all__'

class ProjectDetailSerializer (ProjectSerializer):
        pledges = PledgeSerializer(many=True, read_only=True)
