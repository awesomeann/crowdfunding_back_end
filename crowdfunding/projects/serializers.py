from rest_framework import serializers
from .models import Project, Pledge


class ProjectSerializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Project
        fields = '__all__'

class PledgeSerializer (serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = Pledge
        fields = '__all__'

class ProjectDetailSerializer (ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.animal = validated_data.get('animal', instance.animal)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.save()
        return instance
        

class PledgeDetailSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        return instance        

