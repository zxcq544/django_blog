import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=100, verbose_name='Заголовок новости')
    post_text = models.CharField(max_length=500, verbose_name='Текст новости')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        return timezone.now() - self.pub_date < datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
