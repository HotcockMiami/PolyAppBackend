from django.shortcuts import render
from .serializers import FAQSerializer, ArticleSerializer, CategorySerializer, TagSerializer, CustomUserSerializer, AnswerSerializer, InstructionSerializer, CommentarySerializer
from .models import FAQ, Article, Category, Tag, CustomUser, Answer, Instruction, Commentary
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


class FAQView(APIView):
    def get(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        if pk is None:    
            FAQs = FAQ.objects.all()
        else:
            FAQs = FAQ.objects.filter(pk=pk)
        serializer = FAQSerializer(FAQs, many=True)
        return Response({"FAQs": serializer.data})

    def post(self, request):
        FAQ_post = request.data.get('FAQ')
        serializer = FAQSerializer(data=FAQ_post)
        if serializer.is_valid(raise_exception=True):
            FAQ_saved = serializer.save()
        return Response({"success": "FAQ '{}' created successfully".format(FAQ_saved.title)})

class ArticleView(APIView):
    def get(self,request, pk=None):
        serializer_context = {
            'request': request,
        }
        if pk is None:    
            Articles = Article.objects.all()
        else:
            Articles = Article.objects.filter(pk=pk)
        serializer = ArticleSerializer(Articles, many=True)
        return Response({"Articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

class CategoryView(APIView):
    def get(self,request, pk=None):
        serializer_context = {
            'request': request,
        }
        if pk is None:    
            Categories = Category.objects.all()
        else:
            Categories = Category.objects.filter(pk=pk)
        serializer = CategorySerializer(Categories, many=True)
        return Response({"Categories": serializer.data})

    def post(self, request):
        category = request.data.get('Category')
        serializer = CategorySerializer(data=category)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' created successfully".format(category_saved.title)})

class TagView(APIView):
    def get(self,request, pk=None):
        serializer_context = {
            'request': request,
        }
        if pk is None:    
            Tags = Tag.objects.all()
        else:
            Tags = Tag.objects.filter(pk=pk)
        serializer = TagSerializer(Tags, many=True)
        return Response({"Tags": serializer.data})

    def post(self, request):
        tag = request.data.get('tag')
        serializer = TagSerializer(data=tag)
        if serializer.is_valid(raise_exception=True):
            tag_saved = serializer.save()
        return Response({"success": "Tag '{}' created successfully".format(tag_saved.title)})

class UserView(APIView):
    def get(self,request, pk=None):
        serializer_context = {
            'request': request,
        }
        if pk is None:    
            Users = CustomUser.objects.all()
        else:
            Users = CustomUser.objects.filter(pk=pk)
        serializer = CustomUserSerializer(Users, many=True)
        return Response({"Users": serializer.data})

    def put(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

class AnswerView(APIView):
    def get(self,request, pk=None):
        serializer_context = {
            'request': request,
        }
        if pk is None:    
            Answers = Answer.objects.all()
        else:
            Answers = Answer.objects.filter(pk=pk)
        serializer = AnswerSerializer(Answers, many=True)
        return Response({"Answers": serializer.data})


class InstructionView(APIView):
    def get(self,request, pk=None):
        serializer_context = {
            'request': request,
        }
        if pk is None:    
            Instructions = Instruction.objects.all()
        else:
            Instructions = Instruction.objects.filter(pk=pk)
        serializer = InstructionSerializer(Instructions, many=True, context=serializer_context)
        return Response({"Instructions": serializer.data})

    def post(self, request):
        instruction = request.data.get('Instruction')
        serializer = InstructionSerializer(data=instruction)
        if serializer.is_valid(raise_exception=True):
            instruction_saved = serializer.save()
        return Response({"success": "Instruction '{}' created successfully".format(instruction_saved.title)})

class CommentaryView(APIView):
    def get(self,request, pk=None):
        serializer_context = {
            'request': request,
        }
        if pk is None:    
            Commentaries = Commentary.objects.all()
        else:
            Commentaries = Commentary.objects.filter(pk=pk)
        serializer = CommentarySerializer(Commentaries, many=True)
        return Response({"Commentaries": serializer.data})

    def post(self, request):
        commentary = request.data.get('commentary')
        commentary['user'] = request.user.pk
        serializer = CommentarySerializer(data=commentary)
        if serializer.is_valid(raise_exception=True):
            commentary_saved = serializer.save()
        return Response({"success": "Commentary '{}' created successfully".format(commentary_saved.text)})
