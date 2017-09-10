from django.views.generic import TemplateView
from .models import Post


class HomeView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(active=True)
        return context


class SinglePostView(TemplateView):
    template_name = "app/single_post.html"

    def get_context_data(self, **kwargs):
        context = super(SinglePostView, self).get_context_data(**kwargs)
        # Usually this should be a slug
        pk = self.kwargs.get('pk', None)

        post = Post.objects.filter(pk=pk)

        if not post:
            pass  # TODO: Inform user

        post = post.get()

        if not post.active:
            pass  # TODO: No-go post

        context['post'] = post

        return context
