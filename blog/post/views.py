from django.views.generic import ListView
from models import Post


# Create your views here.

class PostListing(ListView):
    model = Post
