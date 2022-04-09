from django.db import models


class qrcode(models.Model):
    
    qrcodeInput = models.CharField(max_length=20)
    
    def __str__(self):
        return self.qrcodeInput