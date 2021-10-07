from django.contrib import admin
from .models import Editor,Article,tags

# Register your models here.

#create modeladmin that allows us to customize our models inside our admin page
class ArticleAdmin(admin.ModelAdmin):
    #filter property allows ordering of many to many fields and pass in the tags article
    filter_horizontal =('tags',)
    
admin.site.register(Editor)
#article admin subclass as second argument to admin.site.register function
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)