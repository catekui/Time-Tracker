from rest_framework import serializers
 
# import model from models.py
from .models import User,Project,Reviews

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'