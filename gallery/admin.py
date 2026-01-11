from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    """投稿詳細画面でコメントをインライン表示"""
    model = Comment
    extra = 1
    fields = ['text', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """投稿モデルの管理画面設定"""
    list_display = ['title', 'ai_model', 'category', 'created_at']
    list_filter = ['ai_model', 'category', 'created_at']
    search_fields = ['title', 'prompt', 'negative_prompt']
    readonly_fields = ['created_at']
    inlines = [CommentInline]

    fieldsets = (
        ('基本情報', {
            'fields': ('title', 'image', 'category', 'ai_model')
        }),
        ('プロンプト情報', {
            'fields': ('prompt', 'negative_prompt')
        }),
        ('メタ情報', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """コメントモデルの管理画面設定"""
    list_display = ['post', 'text_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text', 'post__title']
    readonly_fields = ['created_at']

    def text_preview(self, obj):
        """コメントのプレビュー表示（最初の50文字）"""
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'コメント内容'
