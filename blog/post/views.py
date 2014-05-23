from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from models import Post


# Create your views here.

class PostListing(ListView):
    model = Post
    template_name = 'post/index.html'
    # content_object_name = 'object_list'
    paginate_by = 2


class PostCreate(CreateView):
    model = Post
    template_name = 'post/new.html'
    success_url = reverse_lazy('post:listing')


class PostDetail(DetailView):
    model = Post
    template_name = 'post/detail.html'


class PostUpdate(UpdateView):
    model = Post
    template_name = 'post/edit.html'

    def get_success_url(self):
        return reverse(
            'post:detail',
            kwargs={
                'pk': self.object.pk,
            }
        )


class PostDelete(DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('post:listing')