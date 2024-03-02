from django import template
from collections import Counter
from django.db.models import F
from django.db.models import Count

register = template.Library()

@register.filter
def get_distinct_service_ty_info(queryset):
    """
    Returns a list of dictionaries containing distinct service types with their counts
    and a list of service objects for each type, sorted alphabetically by service type.

    Args:
        queryset: A QuerySet of Service objects.

    Returns:
        A list of dictionaries: [
            {'service_type': 'type_1', 'count': 5, 'objects': [service_object_1, service_object_2, ...]},
            {'service_type': 'type_2', 'count': 2, 'objects': [service_object_3, service_object_4, ...]},
            ...
        ]
    """
    service_data = []

    # Get distinct service types and their counts
    service_types = queryset.values('service_ty').annotate(count=Count('pk')).order_by('service_ty')

    for service_type in service_types:
        # Fetch objects for each distinct service type
        objects = queryset.filter(service_ty=service_type['service_ty'])
        service_data.append({
            'service_type': service_type['service_ty'],
            'count': service_type['count'],
            'objects': list(objects)
        })

    return service_data






@register.filter
def get_distinct_destinations_ty_info(queryset):
    destination_data = []

    # Get distinct destination types and their counts
    destination_types = queryset.values('destinatio').annotate(count=Count('pk')).order_by('destinatio')

    for destination_type in destination_types:
        # Fetch objects for each distinct destination type
        objects = queryset.filter(destinatio=destination_type['destinatio'])
        destination_data.append({
            'destination_type': destination_type['destinatio'],
            'count': destination_type['count'],
            'objects': list(objects)
        })
    print(destination_data)

    return destination_data