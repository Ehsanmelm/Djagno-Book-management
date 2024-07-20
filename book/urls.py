from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('review' , views.ReviewModelView , basename='review_manage')

urlpatterns = [
    path('book/list' , views.BookListView.as_view() , name='book_list'),
    path('book' , views.BookFilterView.as_view() , name='book_filter_list'),
    path('suggest' , views.BookSuggestView.as_view() , name='book_suggest'),
]

urlpatterns += router.urls
