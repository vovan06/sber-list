from django.db.models import Q


def get_queryset_in_tasks(request, queryset, model, ):
    try:
        parametr = request.query_params['is_ended']
        return queryset.filter(Q(status_id=(int(parametr)+1))) if parametr == '0' or parametr == '1' else model.objects.prefetch_related()
    except:
        return model.objects.prefetch_related()
