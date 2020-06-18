from django.db import models

# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Postcard(models.Model):
    """Model representing a postcard"""

    # has url for dog img
    dog_img_url = models.CharField(max_length=200)

    # has an author
    author = models.CharField(max_length=200, help_text='Your name (optional)')
    
    # has some text
    letter = models.TextField(max_length=1000, help_text='Write love letter here')
    
    # default approval is false
    # will be approved by superuser on admin site
    approved = models.BooleanField(default=False)
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.letter + '\n\nLove,\n' + self.author
    

    def is_approved(self):
        return self.approved == True
    # TODO????
    # not sure what this does
    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this postcard."""
    #     return reverse('postcard-detail', args=[str(self.id)])