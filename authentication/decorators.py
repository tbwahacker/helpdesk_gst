from django.http import HttpResponseForbidden

def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.role not in allowed_roles:
                return HttpResponseForbidden("You are not allowed to access this page")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator