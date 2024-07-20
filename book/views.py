from django.shortcuts import render
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.viewsets import ModelViewSet
from .models import BooksModel , ReviewsModel
from .serializers import BookSerializer , ReviewSerializer
   
# Create your views here.

class BookListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        queryset = BooksModel.objects.all()
        serializer = BookSerializer(queryset , many=True)

        return Response(serializer.data)
    
class BookFilterView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        genre = request.GET.get('genre' , None)

        if genre:
            queryset = BooksModel.objects.filter(genre__icontains=genre)
        
        serializer = BookSerializer(queryset , many = True)
        return Response(serializer.data)
    
class ReviewModelView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = ReviewsModel.objects.filter(user= self.request.user)
        return queryset
    def get_serializer_context(self):
        return {'user_id' : self.request.user.id}


class BookSuggestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        popular_author_list = []

        for review_obj in ReviewsModel.objects.filter(user= self.request.user):

            if review_obj.rating > 3:  # i consider 4 and 5 consider as high score
                popular_author_list.append(review_obj.book.author)
                
        queryset = BooksModel.objects.filter(author__in=popular_author_list)
        serializer = BookSerializer(queryset , many=True)

        return Response(serializer.data)