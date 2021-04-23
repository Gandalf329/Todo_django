from django.db import models

# Create your models here.
class Task(models.Model):
    tittle = models.CharField('tittle', max_length = 250)
    full_task = models.TextField('full_task')
    date = models.DateTimeField('date')

    def __str__(self):
        return self.tittle
    
    def get_absolute_url(self):
        return f'/work/{self.id}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
