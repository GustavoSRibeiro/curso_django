from django.db import models

class Topic(models.Model):
    """"Um Assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em strig do modelo."""
        return self.text
    
class Entry(models.Model):
    """Algo especifico aprendido sobre o assunto."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação em strig do modelo."""
        return self.text[:50] + '...'