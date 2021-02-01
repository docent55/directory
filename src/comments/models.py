from django.db import models

class AbstractComment(models.Model):
    '''Abstract model comments'''
    text = models.TextField('Message', max_length=500)
    created_date = models.DateTimeField('Publication date', auto_now_add=True)
    update_date = models.DateTimeField('Update date', auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        abstract = True
