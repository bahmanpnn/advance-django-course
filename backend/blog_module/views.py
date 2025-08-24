from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from .models import Post
from .forms import PostForm, PostCreateForm


def index(request):
    context = {"name": "bahman pournazari"}
    return render(request, "index.html", context)


class IndexTemplateView(TemplateView):
    """
    remember that templateview just uses for get method and request and does'nt use forms.
    we can use it for simple page with some context with get context data method at the end!!
    """

    template_name = "template_view.html"

    def get_context_data(self, **kwargs):
        print(self.kwargs)
        print(self.kwargs["param"])
        context = super().get_context_data(**kwargs)
        context["name"] = "template view bahmanpn"
        context["posts"] = Post.objects.all()
        return context


def redirect_to_google(request):
    return redirect("http://127.0.0.1:8000")


class RedirectToGoogle(RedirectView):
    url = "http://127.0.0.1:8000"
    # permanent=False / True

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(LoginRequiredMixin, ListView):
    template_name = "post_list.html"  # default template name of this class is post_list.html too and doesnt need to set it again and django find it auto.
    context_object_name = (
        "posts"  # if we dont set it default object name is object list.
    )
    paginate_by = 8

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
    model = Post

    def get_queryset(self):
        query = super().get_queryset().filter(status=True).order_by("id")
        return query


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "post_detail.html"
    model = Post
    # context_object_name='post'

    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)


class PostFormView(LoginRequiredMixin, FormView):
    """
    we dont use form view for having connection with database a lot and it works more for something like sending email for admin or something like that doesnt have any affect on database.
    but i use it to test and save this form and create new object of post model in database.
    """

    template_name = "post_form.html"
    success_url = "/blog/posts"
    form_class = PostForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    """
    https://docs.djangoproject.com/en/5.2/topics/auth/default/
    https://django-tutelary.readthedocs.io/en/latest/usage/permissions-for-views.html

    myuser.groups.set([group_list])
    myuser.groups.add(group, group, ...)
    myuser.groups.remove(group, group, ...)
    myuser.groups.clear()
    myuser.user_permissions.set([permission_list])
    myuser.user_permissions.add(permission, permission, ...)
    myuser.user_permissions.remove(permission, permission, ...)
    myuser.user_permissions.clear()

    #####
    add: user.has_perm('foo.add_bar')

    change: user.has_perm('foo.change_bar')

    delete: user.has_perm('foo.delete_bar')

    view: user.has_perm('foo.view_bar')

    permission mixin give us a permission required and raise_exception attrs to add permissions that we want for this view and endpoint.
    we can override has_permission method of class too.
    def has_permission(self):
        user = self.request.user
        return user.has_perm('blog_module.can_open') or user.has_perm('blog_module.can_edit')
    """

    # permission_required=("blog_module.change_post","blog_module.add_post","blog_module.delete_post","blog_module.get_post")
    # permission_required = {
    #   'GET': None,
    #   'POST': 'board.create'
    # }
    permission_required = "blog_module.add_post"
    raise_exception = True

    model = Post
    form_class = PostCreateForm  # we can use fields attr instead of formclass too,but fields styling handleling is too difficult.
    template_name = "post_create_form.html"
    success_url = "/blog/posts"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "post_create_form.html"
    model = Post
    form_class = PostCreateForm
    success_url = "/blog/posts"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "post_delete_form.html"
    model = Post
    # form_class=PostDeleteForm
    success_url = "/blog/posts"


class BlogListApiView(TemplateView):
    template_name="post_list_api_view.html"