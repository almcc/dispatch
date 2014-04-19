from django.db import models

class Tag(models.Model):
    name = models.CharField(default = '', max_length = 50)
    position = models.IntegerField()
    column = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(default = '', max_length = 100)
    link = models.URLField(default = '', max_length = 400)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.name



