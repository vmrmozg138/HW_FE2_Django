from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .forms import PostForm

# Список постов (только опубликованные)
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')


# Детальная страница поста + счётчик просмотров
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views = obj.views + 1
        obj.save(update_fields=['views'])
        return obj

    def get_queryset(self):
        # Показываем только опубликованные посты
        return Post.objects.filter(is_published=True)

# Создание поста
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post-list')  # куда перенаправить после создания

# Редактирование поста
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.pk})

# Удаление поста
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
