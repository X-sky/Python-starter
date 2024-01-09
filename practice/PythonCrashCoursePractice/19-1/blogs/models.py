from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
