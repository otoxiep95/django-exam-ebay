from functools import wraps
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def check_group(group_name):
    def _check_group(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if request.user.is_anonymous:
                return redirect('/login/')
            if (not (request.user.groups.filter(name=group_name).exists())
                    or request.user.is_superuser):
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_group
