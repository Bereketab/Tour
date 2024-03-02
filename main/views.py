from django.shortcuts import render
from .models import *
from itertools import chain
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from rest_framework import viewsets
from .serializers import DestinationsSerializer, ServicesSerializer

import json


from collections import defaultdict

def getServiceMap(services_data_dict):
    service_mapping = {}
    for item in services_data_dict:
        service_ty = item['fields']['service_ty']
        full_name = item['fields']['full_name']

        if service_ty not in service_mapping:
            service_mapping[service_ty] = []
    
        service_mapping[service_ty].append({'full_name': full_name, 'short_name': item['fields']['short_name']
        # , 'id': item['fields']['id']
        , 'geom': item['fields']['geom']
        , 'objectid': item['fields']['objectid']
        , 'x': item['fields']['x'] 
        , 'y': item['fields']['y']
        , 'z': item['fields']['z']
        , 'code': item['fields']['code']
        , 'zone': item['fields']['zone'] 
        , 'wereda': item['fields']['wereda']
        , 'kebele': item['fields']['kebele']
        , 'phone_line': item['fields']['phone_line']
         , 'email': item['fields']['email']
        , 'website': item['fields']['website'] 
        , 'service_ty': item['fields']['service_ty']
        , 'owner_name': item['fields']['owner_name']
        , 'moto': item['fields']['moto']
        }) 
    return service_mapping

def getDestinationMap(services_data_dict):
    destination_mapping = {}
    for item in services_data_dict:
        destintio = item['fields']['destinatio']
        full_name = item['fields']['full_name']

        if destintio not in destination_mapping:
            destination_mapping[destintio] = []
    
        destination_mapping[destintio].append({'full_name': full_name
                                        #    ,'short_name': item['fields']['short_name']
        # , 'id': item['fields']['id']
        # , 'geom': item['fields']['geom']
        # , 'objectid': item['fields']['objectid']
        # , 'x': item['fields']['x'] 
        # , 'y': item['fields']['y']
        # , 'z': item['fields']['z']
        # , 'code': item['fields']['code']
        # , 'zone': item['fields']['zone'] 
        # , 'wereda': item['fields']['wereda']
        # , 'kebele': item['fields']['kebele']
        # , 'phone_line': item['fields']['phone_line']
        #  , 'email': item['fields']['email']
        # , 'website': item['fields']['website'] 
        # , 'destintio': item['fields']['destintio']
        # , 'owner_name': item['fields']['owner_name']
        # , 'moto': item['fields']['moto']
        }) 
    return destination_mapping

def getFrontData(services_data_dict):
    result = []

    # Sort categories alphabetically
    sorted_categories = sorted(services_data_dict.keys())
    
    for category in sorted_categories:
        category_dict = {
            "text": category,
            "children": []
        }

        # Sort items within the category alphabetically
        sorted_items = sorted(services_data_dict[category], key=lambda x: x["full_name"])

        for item in sorted_items:
            item_dict = {
                "text": item["full_name"]
            }

            category_dict["children"].append(item_dict)
        result.append(category_dict)
    return result


context = {}
def index(request):
        # Assuming you have retrieved data from your models
    destinations = Destinations.objects.all()
    services = Services.objects.all()
    services_data = serializers.serialize("json", services)
    destinations_data = serializers.serialize("json", destinations)

    # Serialize the services data to JSON
    services_data_dict = json.loads(services_data)
    destinations_data_dict = json.loads(destinations_data)
    context['services']=json.dumps(getFrontData(getServiceMap(services_data_dict)), indent=4) 
    context['destinations']=json.dumps(getFrontData(getDestinationMap(destinations_data_dict)), indent=4)  
    combined_data = {
    'services':services ,
    'destinations': destinations
    }
    combined_data_autocomplete = {
    'services': [],
    'destinations': []
    }

    # Extracting services data
    for service in services_data_dict:
        service_dict = {
            'full_name': service['fields']['full_name']
        }
        combined_data_autocomplete['services'].append(service_dict)

    # Extracting destinations data
    for destination in destinations_data_dict:
        destination_dict = {
            'full_name': destination['fields']['full_name']
        }
        combined_data_autocomplete['destinations'].append(destination_dict)
    context['combined_data'] = combined_data
    context['combined_data_autocomplete'] = combined_data_autocomplete
    return render(request,'main/index.html',context)





class DestinationsViewSet(viewsets.ModelViewSet):
    queryset = Destinations.objects.all()
    serializer_class = DestinationsSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer