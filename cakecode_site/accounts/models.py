from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DiscordServer(models.Model):
    is_official = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default="", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 単語帳を作成したユーザーへの外部キー
    star = models.PositiveIntegerField(default=0)  # 「いいね」的なSNS要素
    joined = models.PositiveIntegerField(default=0)
    online = models.PositiveIntegerField(default=0)
    member = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='discord_servers', blank=True)  # タグの多対多の関連
    public = models.BooleanField(default=False, verbose_name="公開する")  # 公開フラグ
    timestamp = models.DateTimeField(auto_now_add=True)
    serverid = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500, default="", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 単語帳を作成したユーザーへの外部キー
    server = models.ForeignKey(DiscordServer, on_delete=models.CASCADE)
    star = models.PositiveIntegerField(default=0)  # 「いいね」的なSNS要素

    def __str__(self):
        return self.title
    
class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ユーザーへの外部キー（1対1）
    user_name = models.CharField(max_length=15, default=user.name)
    user_profile = models.CharField(max_length=60, default="")
    user_icon_url = models.CharField(max_length=300, default="")
    is_official = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name