from rest_framework.decorators import api_view
from rest_framework.response import Response


# Django Rest Framework v1 Endpoints.
@api_view()
def post_list_api_view(request):
    return Response("post list api view")