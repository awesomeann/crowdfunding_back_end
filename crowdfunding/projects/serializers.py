from rest_framework import serializers
from .models import Project, Pledge



class ProjectSerializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    total_number_of_pledges = serializers.ReadOnlyField()
    sum_of_pledges = serializers.ReadOnlyField()
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
    total_number_of_pledges = serializers.ReadOnlyField()
    sum_of_pledges = serializers.ReadOnlyField()
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
    
class ProjectStatusSerializer (ProjectSerializer): 
     def update(self, instance, validated_data):  
          instance.is_successful = validated_data.get('is_successful', instance.is_successful)
          instance.save()
          return instance

class PledgeDetailSerializer(PledgeSerializer):

    def update(self, instance, validated_data):
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous',instance.anonymous)
        instance.project = validated_data.get('project', instance.project)
        instance.save()
        return instance        

