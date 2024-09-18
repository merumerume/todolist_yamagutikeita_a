from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class TodoList(models.Model):
    PRIORITY_CHOICES = [
        ('High', '高'),
        ('Medium', '中'),
        ('Low', '低')
    ]
    
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=255, blank=True, default='記入してください')
    tags = models.ManyToManyField(Tag, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='High')
    comment = models.TextField(blank=True)  # コメントフィールド

    def __str__(self):
        return self.title
