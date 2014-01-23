from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from categories.models import CategoryBase

# TODO: user django-categories


# class Category(models.Model):
#     title = models.CharField(max_length=60)
#     # related_to = models.ManyToManyField('self', blank=True, null=True)
#     related_to = models.ForeignKey('self', blank=True, null=True)

    # def __unicode__(self):
    #     return self.title

    
class Article(models.Model):
    title = models.CharField(max_length=120)
    originator = models.CharField(max_length=60)
    pub_date = models.DateTimeField('date published')
    content = RichTextField()
    category = models.ForeignKey(Category)
    link = models.URLField()
    media = models.TextField()
    tags = TaggableManager()
    category = models.Foreign('categories.Category')
    
    def __unicode__(self):
        return self.title


# Create your models here.


















