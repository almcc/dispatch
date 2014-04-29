from django.db import models

class Task(models.Model):
    STATE_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('stalled', 'Stalled'),
        ('finished', 'Finished')
    )
    name = models.CharField(default = '', max_length = 100)
    description = models.TextField(default = '', blank=True)
    state = models.CharField(default = 'new', max_length = 10, choices=STATE_CHOICES)
    complete = models.IntegerField(default = 0, blank=True)
    link = models.URLField(default = '', max_length = 400, blank=True)
    subtasks = models.ManyToManyField("self", blank=True, symmetrical=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __unicode__(self ):
        return self.name

