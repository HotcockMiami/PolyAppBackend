from rest_framework import serializers
from .models import FAQ, Article, Category, Tag, CustomUser, Answer, Instruction, Commentary

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk', 'first_name', 'last_name', 'country', 'city',
        'group', 'faculty', 'chair', 'is_staff']

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Article
        fields = ['header', 'text', 'tags', 'categories']

    def create(self, validated_data):
        return Article.objects.create(**validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = ['text', 'author', 'categories', 'tags']

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)


class InstructionSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Instruction
        fields = ['text', 'author', 'categories', 'tags']

    def create(self, validated_data):
        return Instruction.objects.create(**validated_data)


class CommentarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Commentary
        fields = ['text', 'user']

    def create(self, validated_data):
        user_id = validated_data.pop('user')
        #user_instance, created = CustomUser.objects.get(pk=user_id.pk)
        return Commentary.objects.create(**validated_data, user=user_id)


class FAQSerializer(serializers.ModelSerializer):
    commentaries = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_answer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    user_question = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'commentaries', 'user_answer', 'user_question', 'category']

    def create(self, validated_data):
        return FAQ.objects.create(**validated_data)
