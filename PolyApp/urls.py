from django.urls import path
from .views import FAQView, ArticleView, CategoryView, TagView, UserView, AnswerView, InstructionView, CommentaryView

urlpatterns = [
    path('faqs/', FAQView.as_view()),
    path('faqs/<int:pk>', FAQView.as_view()),

    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),

    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>', CategoryView.as_view()),

    path('tags/', TagView.as_view()),
    path('tags/<int:pk>', TagView.as_view()),

    path('users/', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),

    path('answers/', AnswerView.as_view()),
    path('answers/<int:pk>', AnswerView.as_view()),

    path('instructions/', InstructionView.as_view()),
    path('instructions/<int:pk>', InstructionView.as_view()),

    path('commentaries/', CommentaryView.as_view()),
    path('commentaries/<int:pk>', CommentaryView.as_view()),
]