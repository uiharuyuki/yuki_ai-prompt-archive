from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    """投稿一覧ビュー"""
    model = Post
    template_name = 'gallery/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """ai_modelとcategoryのGETパラメータで絞り込み"""
        queryset = Post.objects.all()

        # ai_modelでフィルタリング
        ai_model = self.request.GET.get('ai_model')
        if ai_model:
            queryset = queryset.filter(ai_model=ai_model)
        else:
            # デフォルトはDaysAI
            queryset = queryset.filter(ai_model='DaysAI')

        # categoryでフィルタリング
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        else:
            # デフォルトは画像生成
            queryset = queryset.filter(category='Image Generation')

        return queryset


class PostDetailView(DetailView):
    """投稿詳細ビュー"""
    model = Post
    template_name = 'gallery/post_detail.html'
    context_object_name = 'post'
