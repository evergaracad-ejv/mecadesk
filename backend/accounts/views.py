from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and (request.user.role in allowed_roles or request.user.is_superuser):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator

@login_required
@role_required(allowed_roles=['admin'])
def dashboard_admin_view(request):
    return JsonResponse({'message': 'Acceso autorizado para Administrador', 'user': request.user.username})

@login_required
@role_required(allowed_roles=['admin', 'gestor'])
def dashboard_gestor_view(request):
    return JsonResponse({'message': 'Acceso autorizado para Gestor o Admin', 'user': request.user.username})

@login_required
@role_required(allowed_roles=['admin', 'gestor', 'usuario', 'mecanico'])
def dashboard_mecanico_view(request):
    return JsonResponse({'message': 'Acceso autorizado para Mecánico / Usuario', 'user': request.user.username})