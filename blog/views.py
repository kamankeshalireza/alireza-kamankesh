from django.shortcuts import render

def index_view(request):
    context = {'page_title': 'Home'}
    return render(request, 'blog/index.html', context)

def about_view(request):
    context = {'page_title': 'About Me'}
    return render(request, 'blog/about.html', context)

def resume_view(request):
    context = {'page_title': 'Resume'}
    return render(request, 'blog/resume.html', context)

def services_view(request):
    context = {'page_title': 'Services'}
    return render(request, 'blog/services.html', context)

def portfolio_view(request):
    context = {'page_title': 'Portfolio'}
    return render(request, 'blog/portfolio.html', context)

def contact_view(request):
    context = {'page_title': 'Contact'}
    return render(request, 'blog/contact.html', context)