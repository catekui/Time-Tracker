from rest_framework import serializers
 
# import model from models.py
from .models import Time_Worked,Project,Reviews,Activity,User

     
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        include = ["profession","image","name"]
   
     
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
                
       
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        

class TimeWorkedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_Worked
        fields = '__all__'



class ReviewsSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    class Meta:
        model = Reviews
        fields = '__all__'

     
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class UserSerializer1(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }