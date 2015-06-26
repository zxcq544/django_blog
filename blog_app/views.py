from django.contrib.auth.decorators import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic

from .models import Post, Comment


class IndexView(generic.ListView):
    template_name = 'blog_app/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.filter(pub_date__lte=timezone.now).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog_app/detail.html'

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Post
    template_name = 'blog_app/results.html'


def vote(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    try:
        selected_comment = p.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the post voting form.
        return render(request, 'blog_app/detail.html', {
            'post': p,
            'error_message': "You didn't select a comment.",
        })
    else:
        selected_comment.votes += 1
        selected_comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog_app:results', args=(p.id,)))
