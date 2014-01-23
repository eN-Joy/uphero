from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from categories.models import CategoryBase


class Category(CategoryBase):
    pass
    # title = models.CharField(max_length=60)

    # def __unicode__(self):
    #     return self.title
# class Category(models.Model):
#     title = models.CharField(max_length=60)
#     # related_to = models.ManyToManyField('self', blank=True, null=True)
#     related_to = models.ForeignKey('self', blank=True, null=True)

#     def __unicode__(self):
#         return self.title


class Article(models.Model):
    title = models.CharField(max_length=120)
    originator = models.CharField(max_length=60)
    pub_date = models.DateTimeField('date published')
    content = RichTextField()
    category = models.ForeignKey(Category)
    link = models.URLField()
    media = models.TextField()
    tags = TaggableManager()
    category = models.ForeignKey('categories.Category')
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title


# Create your models here.
