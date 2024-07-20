from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import BooksModel , ReviewsModel

class BookSerializer(ModelSerializer):
    class Meta:
        model = BooksModel
        fields = ['id' , 'title' , 'author' , 'genre']

class ReviewSerializer(ModelSerializer):
    user_id = serializers.IntegerField(read_only = True)
    # book = BookSerializer()
    class Meta:
        model= ReviewsModel
        fields = ['id' , 'book' , 'user_id' , 'rating']

    def create(self, validated_data):
        user_id = self.context['user_id']

        return ReviewsModel.objects.create(user_id=user_id , **validated_data)
