from django.conf import settings
from django.db import models
from django.utils import timezone

#Definición de modelo (objetos)
class Post(models.Model): 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) #Es una relación (link)
    title = models.CharField(max_length=200) #Definición de un texto con un número de carateres limitados
    text = models.TextField() #Define el texto largo sin límite
    created_date = models.DateTimeField(default=timezone.now) #Define fecha y hora
    published_date = models.DateTimeField(blank=True, null=True) 

    def publish(self): 
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
