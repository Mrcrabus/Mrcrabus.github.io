from abc import ABC
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import News
from .forms import NewsImage


def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Main page of block'
    }
    return render(request, 'blog/home.html', data)


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, ABC):
    model = News
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)
        ctx['title'] = "Main page"
        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(UserAllNewsView, self).get_context_data(**kwargs)
        ctx['title'] = f"All articles by {self.kwargs.get('username')}"
        return ctx


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ABC):
    model = News
    fields = ['title', 'text', 'img']

    def update_img(self, request):
        news_img = NewsImage(request.POST, request.FILES)
        if request.method == 'POST':
            news_img.save()
            if news_img.is_valid():
                news_img.save()
                return redirect('home_new')
            else:
                news_img = NewsImage()
            return render(request, 'blog/news_detail.html', {'form': news_img})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'text', 'img']
    context_object_name = 'home'

    def load_img(self, request):
        if request.method == 'POST':
            news_img = NewsImage(request.POST, request.FILES)
            if news_img.is_valid():
                news_img.save()
                return redirect('home')
        else:
            news_img = NewsImage()
        return render(request, 'blog/news_form.html', {'form': news_img})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def block(request):
    return render(request, 'blog/block.html', {'title': 'Page about us'})
