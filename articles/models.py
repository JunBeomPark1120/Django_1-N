from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    # 용어 설명
    # pk : 기본키라 하여, 고유한 값 설정하는 키
    # fk : 외래키라 하여, 나의 고유한 값은 아니지만 M:N 관계에서 자주 쓰이는 키