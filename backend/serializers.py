from rest_framework import serializers
from backend.models import public_book_data

class Data1(serializers.ModelSerializer):
    class Meta:
        model = public_book_data
        fields = '__all__'
 