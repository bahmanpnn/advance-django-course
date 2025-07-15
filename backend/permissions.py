from rest_framework.permissions import BasePermission,SAFE_METHODS



class IsAuthorOrReadOnlyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(obj.__dict__)
        if request.method in SAFE_METHODS:
            return True
        return obj.author.id == request.user.id or request.user.is_superuser



# class BlackListPermission(BasePermission):
#     """Global permission for blacklist IPs"""
#     def has_permission(self, request, view):
#         ip_addr=request.META['REMOTE_ADDR']
#         blocked=BlackList.objects.filter(ip_addr=ip_addr).exists()
#         return not blocked