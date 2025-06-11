from rest_framework import serializers
from .models import *

class Bookseralizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_price(self,value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than or equal to 0")
        return value 
    # def validate(self,data):
