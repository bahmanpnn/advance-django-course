from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name='blog_module'
urlpatterns = [
    path('fbv-index/',views.index,name='fbv-index'),

    path('templateview-index/',TemplateView.as_view(template_name="index.html",extra_context={"name":"bahman"}),name='templateview-index'),
    # path('cbv-templateview-index/',views.IndexTemplateView.as_view(),name='cbv-templateview-index'),
    path('cbv-templateview-index/<str:param>',views.IndexTemplateView.as_view(),name='cbv-templateview-index'),

    # Redirect-view
    # Permanent false means status code 302(temporary redirecting) but default is true and status code 301(its not temporary redirecting)
    path('go-to-google/',RedirectView.as_view(url="http://127.0.0.1:8000/blog/cbv-templateview-index/test"),name='redirectview-one'),
    path('go-to-google-two/',RedirectView.as_view(pattern_name="blog_module:fbv-index"),name='redirectview-two'),
    path('go-to-google-three/',RedirectView.as_view(pattern_name="blog_module:fbv-index",permanent=True),name='redirectview-three'),
    
    path('fbv-go-to-google/',views.redirect_to_google,name='fbv-redirectview'),
    path('cbv-go-to-google/<int:pk>/',views.RedirectToGoogle.as_view(),name='cbv-redirectview'),

    # List view + Detail view
    path('posts/',views.PostListView.as_view(),name='post-list'),
    path('post-detail/<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),

    # Form view + Create view
    path('posts/form-view/',views.PostFormView.as_view(),name='post-form'),
    path('posts/create-view/',views.PostCreateView.as_view(),name='post-create-form'),

]
