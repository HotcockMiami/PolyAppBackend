from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Category(models.Model):
    name = models.TextField(verbose_name='Имя категории')
    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.TextField(verbose_name='Имя тега')
    class Meta:
        verbose_name_plural = "Тэги"
        verbose_name = "Тэг"
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    country = models.TextField(verbose_name='Страна')
    city = models.TextField(verbose_name='Город')
    group = models.TextField(verbose_name='Учебная группа', null=True, blank=True)
    faculty = models.TextField(verbose_name='Факультет', null=True, blank=True)
    chair = models.TextField(verbose_name='Кафедра', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Article(models.Model):
    header = models.TextField(verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    categories = models.ForeignKey(Category, on_delete=SET_DEFAULT, default=0, verbose_name='Категории')

    class Meta:
        verbose_name_plural = "Статьи"
        verbose_name = "Статья"

    def __str__(self):
        return self.header

class Answer(models.Model):
    text = models.TextField(verbose_name='Текст шаблона')
    author = models.ForeignKey(CustomUser, on_delete=SET_DEFAULT, default=0)
    categories = models.ForeignKey(Category, on_delete=SET_DEFAULT, default=0)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = "Ответы"
        verbose_name = "Ответ"

    def __str__(self):
        return self.text

class Instruction(models.Model):
    text = models.TextField(verbose_name='Текст инструкции')
    author = models.ForeignKey(CustomUser, on_delete=SET_DEFAULT, default=0, verbose_name='Автор')
    categories = models.ForeignKey(Category, on_delete=SET_DEFAULT, default=0, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')

    class Meta:
        verbose_name_plural = "Инструкции"
        verbose_name = "Инструкция"

    def __str__(self):
        return self.text

class Commentary(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    user = models.ForeignKey(CustomUser, on_delete=SET_DEFAULT, default=0, verbose_name='Пользователь')

    class Meta:
        verbose_name_plural = "Комментарии"
        verbose_name = "Комментарий"

    def __str__(self) -> str:
        return self.text

class FAQ(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    commentaries = models.ManyToManyField(Commentary, blank=True, verbose_name='Комментарии')
    user_answer = models.ForeignKey(CustomUser, on_delete=SET_DEFAULT, default=0, related_name='user_id_answer', verbose_name='Ответивший пользователь')
    user_question = models.ForeignKey(CustomUser, on_delete=SET_DEFAULT, default=0, related_name='user_id_question', verbose_name='Спросившний пользователь')
    category = models.ForeignKey(Category, on_delete=SET_DEFAULT, default=0, related_name='category', verbose_name='Категория')
    is_answered = models.BooleanField(default=False, verbose_name='Есть ответ на вопрос?')
    
    class Meta:
        verbose_name_plural = "FAQs"
        verbose_name = "FAQ"

    def save(self, *args, **kwargs):
        print(self.answer)
        if self.answer != "":
            self.is_answered=True
        super(FAQ, self).save(*args, **kwargs)
    def __str__(self):
        return self.question

class AnswerTemplate(models.Model):
    text = models.TextField(verbose_name='Текст шаблона')
    author = models.ForeignKey(CustomUser, on_delete=SET_DEFAULT, default=0, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=SET_DEFAULT, default=0, verbose_name='Категория')

    class Meta:
        verbose_name_plural = "Шаблоны ответа"
        verbose_name = "Шаблон ответа"

    def __str__(self):
        return self.text