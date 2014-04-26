from django.db import models

class Task(models.Model):
    STATE_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('stalled', 'Stalled'),
        ('finished', 'Finished')
    )
    name = models.CharField(default = '', max_length = 100)
    description = models.TextField()
    state = models.CharField(default = 'default', max_length = 10, choices=STATE_CHOICES)
    complete = models.IntegerField()
    link = models.URLField(default = '', max_length = 400)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

