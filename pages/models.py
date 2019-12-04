from django.db import models


class Slide(models.Model):
    CAPTION_STYLE_CHOICES = [
        ('caption left-align', 'Baslık Solda'),
        ('caption right-align', 'Baslık Sagda'),
        ('caption center-align', 'Baslık Ortada'),
    ]
    slideImage = models.ImageField(upload_to='slide_images/')
    caption = models.CharField(max_length=50)
    captionStyle = models.CharField(max_length=25,choices=CAPTION_STYLE_CHOICES,default="caption left-align")

    def __str__(self):
        return self.caption

class ImageCard(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    cardImage = models.ImageField(upload_to='card_images/')

    def __str__(self):
        return self.title


