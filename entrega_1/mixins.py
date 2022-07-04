from django.shortcuts import render 

class Admin_mixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return render(request, 'insufficient_permissions.html')