from django.http import HttpResponseForbidden


def hasRole(argument):
    def roleDecorator(function):
        def wrapper(*args, **kwargs):
            roles = argument.split(",")
            role = args[0].user.role
            if (role is None) or not any(role.role_name in s for s in roles):
                return HttpResponseForbidden()
            result = function(*args, **kwargs)
            return result

        return wrapper

    return roleDecorator
