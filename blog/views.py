from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import ContactForm
from .models import Post


def _published():
    return Post.objects.filter(is_published=True, published_at__lte=timezone.now())


def index_view(request):
    return render(request, 'blog/index.html', {'latest_posts': _published()[:3]})


def about_view(request):
    return render(request, 'blog/about.html')


def resume_view(request):
    return render(request, 'blog/resume.html')


def services_view(request):
    return render(request, 'blog/services.html')


def portfolio_view(request):
    return render(request, 'blog/portfolio.html')


def contact_view(request):
    form_sent = False
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form_sent = True
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form, 'form_sent': form_sent})


def blog_list_view(request):
    return render(request, 'blog/post_list.html', {'posts': _published()})


def post_detail_view(request, slug):
    post = get_object_or_404(_published(), slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
