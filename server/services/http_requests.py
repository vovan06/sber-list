from rest_framework.response import Response
from rest_framework import status

def _post(request, get_serializer, perform_create, model, get_only_serializer):
    serializer = get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    perform_create(serializer)
    return Response(get_only_serializer(model.objects.get(id=serializer.data['id'])).data, status=status.HTTP_201_CREATED)

def _put(request, get_serializer, get_object, perform_update, model, get_only_serializer, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = get_object()
    serializer = get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
        instance._prefetched_objects_cache = {}

    return Response(get_only_serializer(model.objects.get(id=serializer.data['id'])).data, status=status.HTTP_202_ACCEPTED)

def _update(request, get_object, get_serializer, perform_update, model, get_only_serializer, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = get_object()
    serializer = get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
        instance._prefetched_objects_cache = {}

    return Response(get_only_serializer(model.objects.get(id=serializer.data['id'])).data, status=status.HTTP_202_ACCEPTED)

def _destroy(request, get_object, perform_destroy, *args, **kwargs):
    instance = get_object()
    perform_destroy(instance)
    return Response(status=status.HTTP_204_NO_CONTENT)
