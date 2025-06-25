from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('fbv-index/',views.index,name='fbv-index'),
    path('templateview-index/',TemplateView.as_view(template_name="index.html",extra_context={"name":"bahman"}),name='templateview-index'),
    
    # path('cbv-templateview-index/',views.IndexTemplateView.as_view(),name='cbv-templateview-index'),
    path('cbv-templateview-index/<str:param>',views.IndexTemplateView.as_view(),name='cbv-templateview-index'),

    
]
