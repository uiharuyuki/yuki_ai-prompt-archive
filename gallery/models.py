from django.db import models


class Post(models.Model):
    """投稿データモデル"""

    AI_MODEL_CHOICES = [
        ('DaysAI', 'DaysAI'),
        ('nanobanana', 'nanobanana'),
    ]

    CATEGORY_CHOICES = [
        ('Image Generation', '画像生成'),
        ('Image Correction', '画像修正'),
    ]

    title = models.CharField(max_length=200, blank=True, verbose_name='タイトル')
    image = models.ImageField(upload_to='images/', verbose_name='画像')
    prompt = models.TextField(verbose_name='プロンプト')
    negative_prompt = models.TextField(blank=True, verbose_name='ネガティブプロンプト')
    ai_model = models.CharField(max_length=50, choices=AI_MODEL_CHOICES, verbose_name='AIモデル')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='カテゴリー')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')

    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿一覧'
        ordering = ['-created_at']

    def __str__(self):
        return self.title if self.title else f'Post {self.id}'


class Comment(models.Model):
    """コメント・メモモデル"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='投稿')
    text = models.TextField(verbose_name='コメント')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント一覧'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.post} - {self.text[:30]}'
