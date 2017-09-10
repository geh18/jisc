from django.views.generic import TemplateView
from django.db.models import F

from .models import Post



class HomeView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        posts = Post.objects.filter(active=True)

        sort_by = self.kwargs.get('sort', None)

        if sort_by == '1':
            posts = posts.order_by('-publish')
        elif sort_by == '2':
            posts = posts.order_by('-viewed')

        context['posts'] = posts

        return context


class SinglePostView(TemplateView):
    template_name = "app/single_post.html"

    def get_context_data(self, **kwargs):
        context = super(SinglePostView, self).get_context_data(**kwargs)
        # Usually this should be a slug
        pk = self.kwargs.get('pk', None)

        post = Post.objects.filter(pk=pk)

        post.update(viewed=F('viewed') + 1)

        if post:
            post = post.get()

        if post and not post.active:
            pass

        context['post'] = post

        return context
