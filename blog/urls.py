from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('resume/', views.resume_view, name='resume'),
    path('services/', views.services_view, name='services'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('blog/', views.blog_list_view, name='blog_list'),
    path('blog/<str:slug>/', views.post_detail_view, name='post_detail'),
    path('contact/', views.contact_view, name='contact'),
]
