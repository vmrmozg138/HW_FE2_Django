from django.core.exceptions import PermissionDenied


class OwnerRequiredMixin:
    owner_field = "owner"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        owner = getattr(obj, self.owner_field)
        if owner != request.user and not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
