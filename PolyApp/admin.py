from django.contrib import admin
from .models import FAQ, Article, Category, Tag, CustomUser, Answer, Instruction, Commentary
# Register your models here.

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_answered',)
    list_filter = ('is_answered',)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)

admin.site.register(FAQ, FAQAdmin)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Answer)
admin.site.register(Instruction)
admin.site.register(Commentary)
