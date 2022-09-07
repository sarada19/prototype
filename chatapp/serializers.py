from rest_framework import serializers
from .models import *

class list_post(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'