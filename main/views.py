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

def index(request):
    return render(request,'main/landing.html',context)
context = {}
def app(request):
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
             'id': service['pk'],
            'geom': service['fields']['geom'],
            'objectid': service['fields']['objectid'],
            'x': service['fields']['x'],
            'y': service['fields']['y'],
            'z': service['fields']['z'],
            'code': service['fields']['code'],
            'full_name': service['fields']['full_name'],
            'short_name': service['fields']['short_name'],
            'zone': service['fields']['zone'],
            'wereda': service['fields']['wereda'],
            'kebele': service['fields']['kebele'],
            'phone_line': service['fields']['phone_line'],
            'email': service['fields']['email'],
            'website': service['fields']['website'],
            'service_ty': service['fields']['service_ty'],
            'owner_name': service['fields']['owner_name'],
            'moto': service['fields']['moto']

        }
        combined_data_autocomplete['services'].append(service_dict)

    # Extracting destinations data
    for destination in destinations_data_dict:
        destination_dict = {
        'id': destination['pk'],
        'geom': destination['fields']['geom'],
        'objectid': destination['fields']['objectid'],
        'name': destination['fields']['name'],
        'datetimes': destination['fields']['datetimes'],
        'elevation': destination['fields']['elevation'],
        'code': destination['fields']['code'],
        'full_name': destination['fields']['full_name'],
        'short_name': destination['fields']['short_name'],
        'zone': destination['fields']['zone'],
        'wereda': destination['fields']['wereda'],
        'kebele': destination['fields']['kebele'],
        'locality_n': destination['fields']['locality_n'],
        'organizati': destination['fields']['organizati'],
        'destinatio': destination['fields']['destinatio'],
        'status': destination['fields']['status'],
        'area_sqkm': destination['fields']['area_sqkm'],
        'yearly_est': destination['fields']['yearly_est'],
        'unesco_reg': destination['fields']['unesco_reg'],
        'descriptio': destination['fields']['descriptio'],
        'photo_no': destination['fields']['photo_no'],
        'photo_loca': destination['fields']['photo_loca'],
        'site_des_a': destination['fields']['site_des_a'],
        'amharic': destination['fields']['amharic'],
        'english': destination['fields']['english'],
        'x': destination['fields']['x'],
        'y': destination['fields']['y'],
        'image1': destination['fields']['image1'],
        'image2': destination['fields']['image2']
            

        }
        combined_data_autocomplete['destinations'].append(destination_dict)
    context['combined_data'] = combined_data
    context['combined_data_autocomplete'] = json.dumps(combined_data_autocomplete)
    return render(request,'main/index.html',context)





class DestinationsViewSet(viewsets.ModelViewSet):
    queryset = Destinations.objects.all()
    serializer_class = DestinationsSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer