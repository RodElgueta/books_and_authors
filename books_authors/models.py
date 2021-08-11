from django.db import models

# Create your models here.
class Books(models.Model):
	
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=455)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __repr__(self) -> str:
        return f'{self.id},{self.title}'

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField(Books, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=255,default="notas antiguos")

    def __repr__(self) -> str:
        return f'{self.id},{self.first_name}'