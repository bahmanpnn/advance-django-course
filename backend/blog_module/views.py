from django.shortcuts import render
from django.views.generic.base import TemplateView
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