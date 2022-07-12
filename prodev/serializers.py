from rest_framework import serializers
 
# import model from models.py
from .models import Time_Worked, User,Project,Reviews,Activity

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
       
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        
        exclude = ['image']
        
        # extra_kwargs = {
        #     'password':{'write_only':True}
        # }
    # def create (self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         user.password = make_password('password')
    #     instance.save()
    #     return instance
     
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
        
class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'       
        
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        

class TimeWorkedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_Worked
        fields = '__all__'
