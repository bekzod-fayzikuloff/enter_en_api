from django.db.models import Model, QuerySet


def include_queryset(model: type[Model], *filter_args, **filter_kwargs) -> QuerySet[type[Model]]:
    return model.objects.filter(*filter_args, **filter_kwargs)
