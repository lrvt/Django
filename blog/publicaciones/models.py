from django.db import models


class Posts(models.Model):
    title = models.CharField(verbose_name='Titulo de la publicacion', max_length=150)
    content = models.TextField(verbose_name='Agrega el contenido de la publicación')
    status = models.SmallIntegerField(verbose_name='Indica el estado de la publicación')
    publishedDate = models.DateTimeField('Especificar fecha de publicación')
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name ='Publicacion'
        verbose_name_plural = 'Publicaciones'