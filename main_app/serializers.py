from rest_framework import serializers
from .models import Cat, Feeding, Toy
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    # SerializerMethodField to use a custom method for the field
    fed_for_today = serializers.SerializerMethodField()
    toys = ToySerializer(many=True, read_only=True) # Nested serializer for the 'toys' field
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Make the user field read-only


    class Meta:
        model = Cat
        fields = '__all__'  # Include all fields of the Cat model in the serializer

    # Define the method to get the value for the 'fed_for_today' field
    def get_fed_for_today(self, obj):
        # Call the fed_for_today method of the Cat model to determine if the cat was fed today
        return obj.fed_for_today()

class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'  # Include all fields of the Feeding model in the serializer
        read_only_fields = ['cat',]  # Prevent 'cat' field from being modified directly

        # By marking 'cat' as read-only, we ensure it cannot be set directly through the API
        # This helps maintain data integrity, as the 'cat' relationship should not be changed casually
