from django.db import models


class Message(models.Model):
    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.message_text
        
class Like(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.message
