from django.db import models

PRIORITY_CHOICES = sorted([('low', 'Low'),('average', 'Average'),('high', 'High')])


class Projects(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    assignedDate = models.DateField()
    resource = models.CharField(max_length=100, blank=True, default='')
    priority = models.CharField(choices=PRIORITY_CHOICES, default='Low', max_length=100)
    description = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['name']
