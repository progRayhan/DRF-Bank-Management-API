from rest_framework import serializers
from bank_app.models import Bank, UserProfile

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    bank_is = BankSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password', 'bank_is')
        extra_kwargs = {'password':{'write_only':True}}
        
        def create(self,validated_data):
            user = UserProfile(
                email=validated_data['email'],
                name=validated_data['name'],
            )
            
            user.set_password(validated_data['password'])
            user.save()
            
            return user
