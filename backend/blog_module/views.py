from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView,RedirectView
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
