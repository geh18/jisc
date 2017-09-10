from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from app.models import Post



class Command(BaseCommand):
    help = 'Sends email with the latest posts'

    def add_arguments(self, parser):
        parser.add_argument('post_id', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        post_id = kwargs['post_id'][0]
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise CommandError('Post "%s" does not exist' % post_id)

        # subject, from_email, to = post.title , 'adric.warth@jisc.ac.uk', 'Django.test@example.com'
        subject, from_email, to = post.title, 'gezim913@gmail.com', 'gezim913@gmail.com'

        html_content = render_to_string('email/post.html', {'post': post})
        text_content = strip_tags(html_content)

        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
