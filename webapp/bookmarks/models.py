from django.db import models

class Page(models.Model):
    name = models.CharField(default = '', max_length = 50)
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __unicode__(self):
        return self.name


class Tag(models.Model):
    COLOUR_CHOICES = (
        ('default', 'Grey'),
        ('primary', 'Blue'),
        ('success', 'Green'),
        ('info', 'Aqua'),
        ('warning', 'Yellow'),
        ('danger', 'Red'),
    )
    name = models.CharField(default = '', max_length = 50)
    position = models.IntegerField()
    column = models.IntegerField()
    colour = models.CharField(default = 'default', max_length = 10, choices=COLOUR_CHOICES)
    page = models.ForeignKey(Page)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __unicode__(self):
        return self.name


class Link(models.Model):
    COLOUR_CHOICES = (
        ('default', 'White'),
        ('success', 'Green'),
        ('info', 'Aqua'),
        ('warning', 'Yellow'),
        ('danger', 'Red'),
    )
    name = models.CharField(default = '', max_length = 100)
    link = models.URLField(default = '', max_length = 400)
    colour = models.CharField(default = 'default', max_length = 10, choices=COLOUR_CHOICES)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __unicode__(self):
        return self.name
