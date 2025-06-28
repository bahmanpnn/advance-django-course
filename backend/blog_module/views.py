from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView,DetailView
from .models import Post

def index(request):
    context={
        "name":"bahman pournazari"
    }
    return render(request,'index.html',context)


class IndexTemplateView(TemplateView):
    """
        remember that templateview just uses for get method and request and does'nt use forms.
        we can use it for simple page with some context with get context data method at the end!!
    """

    template_name="template_view.html"
    def get_context_data(self, **kwargs):
        print(self.kwargs)
        print(self.kwargs['param'])
        context=super().get_context_data(**kwargs)
        context['name']="template view bahmanpn"
        context['posts']=Post.objects.all()
        return context


def redirect_to_google(request):
    return redirect("http://127.0.0.1:8000")

class RedirectToGoogle(RedirectView):
    url="http://127.0.0.1:8000"
    # permanent=False / True

    def get_redirect_url(self, *args, **kwargs):
        post=get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

class PostListView(ListView):
    template_name='post_list.html' # default template name of this class is post_list.html too and doesnt need to set it again and django find it auto.
    context_object_name="posts" # if we dont set it default object name is object list.
    paginate_by=2

    # ordering='-id' # remember that it has conflict with queryset and cant have both at a time and we can just have it when set model attr.
    # model=Post
    
    # if we want to filter post and model we can't use model and must use queryset attr instead of model
    # queryset=Post.objects.all()
    
    # or if we need more complex filtering on model we can use get_queryset method and override it. 
    # def get_queryset(self):
    #     # posts=Post.objects.filter(status=True)
    #     posts=Post.objects.filter(status=True).order_by('-id')
    #     return posts
    
    # if we want to use both(model + queryset) must use super.
    model=Post
    def get_queryset(self):        
        query=super().get_queryset().filter(status=True).order_by('id')
        return query
    