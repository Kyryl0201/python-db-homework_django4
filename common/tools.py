from functools import wraps
from django.core.exceptions import PermissionDenied


def group_required(group_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied

            if not request.user.groups.filter(name=group_name).exists():
                raise PermissionDenied

            return func(request, *args, **kwargs)

        return wrapper
    return decorator
