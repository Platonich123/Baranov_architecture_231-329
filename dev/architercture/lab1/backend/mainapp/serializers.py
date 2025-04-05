from rest_framework import serializers

from .models import Monowheel

class MonowheelSeriallizer(serializers.ModelSerializer):
    
    class Meta:
        model = Monowheel
        fields = '__all__'
        #exclude = ['']