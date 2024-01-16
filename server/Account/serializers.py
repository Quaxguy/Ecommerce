from rest_framework import  serializers
from  Account.models import User
# from Account.utils import Utils

import uuid
from rest_framework import serializers
from Account.models import User
import uuid


class UserRegistrationSerializers(serializers.ModelSerializer):
    email_token = serializers.CharField(max_length=200, read_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'phone_number', 'password2', 'email_token']
        extra_kwargs = {
            'password': {'write_only': True}
        }



    def create(self,validated_data):
         email_token=str(uuid.uuid4())
         password = validated_data.pop('password')
         password2 = validated_data.pop('password2')
         if password != password2:
            raise serializers.ValidationError("Password and confirm password don't match")
         email = validated_data.get('email', None)
         if email is None:
          raise serializers.ValidationError("Email is required")
         # Remove 'email' from validated_data to avoid duplicate arguments
        #  validated_data.pop('email', None)
         validated_data['email_token']=email_token
         user = User.objects.create_user(**validated_data)
         return user

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']   
          