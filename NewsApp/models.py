from django.db import models
from django.utils import timezone
from rest_framework.serializers import ModelSerializer


CHOICES_NAME = [
    (1, 'سیاست'),
    (2, 'فرهنگ و هنر'),
    (3, 'اقتصاد'),
    (4, 'جهان'),
    (5, 'ورزش'),
    (6, 'جنگ نرم'),
    (7, 'جهاد و مقاومت'),
    (8, 'بازار'),
    (9, 'دفاع و امنیت'),
]


class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images')
    shortDescription = models.TextField(max_length=300)
    description = models.TextField(max_length=100000)
    # category = models.IntegerField(choices=CHOICES_NAME, default=1)
    # dateOfRelease = models.DateTimeField(db_index=True, default=timezone.now)

    def __str__(self):
        return self.title
    


class NewsSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'



        