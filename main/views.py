from django.shortcuts import render
from .models import *
from itertools import chain
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from rest_framework import viewsets
from .serializers import DestinationsSerializer, ServicesSerializer

import json
from django.http import HttpResponse

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
        #                                    ,'short_name': item['fields']['short_name']
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
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import geojson

@csrf_exempt
def shortest_path(request):
    source = request.POST['source']
    target = request.POST['target']
    with connection.cursor() as cursor:
        query = """
        SELECT
          min(r.seq) AS seq,
          e.old_id AS id,
          e.name,
          sum(e.distance) AS distance,
          ST_AsGeoJSON(ST_Collect(e.the_geom)) AS geom
        FROM
          pgr_dijkstra(
            'SELECT id, source, target, distance AS cost FROM edges_noded',
            %s::integer, %s::integer, false::boolean
          ) AS r,
          edges_noded AS e
        WHERE
          r.edge = e.id
        GROUP BY
          e.old_id, e.name;
        """
        cursor.execute(query, [source, target])
        rows = cursor.fetchall()

    # Ensure there is a result
    if rows:
        features = []
        for row in rows:
            features.append({
                "type": "Feature",
                "properties": {
                    "seq": row[0],
                    "id": row[1],
                    "name": row[2],
                    "distance": row[3]
                },
                "geometry": json.loads(row[4])
            })
        # Return the GeoJSON LineString object
        return JsonResponse({
            "type": "FeatureCollection",
            "features": features
        })
    else:
        return JsonResponse({"error": "No path found"}, status=404)
 




def getBoundary():
    with connection.cursor() as cursor:
        query = """
            SELECT ST_AsGeoJSON(geom)::json AS geojson
    FROM projectedsouthomo;
            """
        cursor.execute(query)
        row = cursor.fetchone()
    return row
    
def return_nearestV(x,y):
    with connection.cursor() as cursor:
            query = """
        SELECT
            v.id,
            ST_AsGeoJSON(v.the_geom) AS geom
        FROM
            edges_noded_vertices_pgr AS v,
            edges_noded AS e
        WHERE
            v.id = (
                SELECT
                    id
                FROM
                    edges_noded_vertices_pgr
                ORDER BY
                    the_geom <-> ST_SetSRID(ST_MakePoint(%s, %s), 4326)
                LIMIT 1
            )
            AND (e.source = v.id OR e.target = v.id)
        GROUP BY v.id, v.the_geom;
        """
            cursor.execute(query, [x, y])
            row = cursor.fetchone()
    return row
@csrf_exempt
def getNearstVertex(request):
    selected_item = json.loads(request.POST['selectedItem'])
    x=selected_item['x']
    y=selected_item['y']   
    row =return_nearestV(x,y)
    if row:
        if selected_item['whattype']=='services':
            point = geojson.Point(geojson.loads(row[1])['coordinates'])
            feature = geojson.Feature(geometry=point, properties={"id": row[0],
                                                                "whattype": selected_item['whattype'],
                    "objectid": selected_item['objectid'],
                    "x": selected_item['x'],
                    "y": selected_item['y'],
                    "z": selected_item['z'],
                    "code": selected_item['code'],
                    "full_name": selected_item['label'],
                    "short_name": selected_item['short_name'],
                    "zone": selected_item['zone'],
                    "wereda": selected_item['wereda'],
                    "kebele": selected_item['kebele'],
                    "phone_line": selected_item['phone_line'],
                    "email": selected_item['email'],
                    "website": selected_item['website'],
                    "service_ty": selected_item['service_ty'],
                    "owner_name": selected_item['owner_name'],
                    "moto": selected_item['moto']})
            return JsonResponse(feature)
        if selected_item['whattype']=='destinations':
            print(True)
            point = geojson.Point(geojson.loads(row[1])['coordinates'])
            feature = geojson.Feature(geometry=point, properties={"id": row[0],
                                                                "whattype": selected_item['whattype'],

                                                                #  'id': destination['pk'],
        'objectid': selected_item['objectid'],
        'name': selected_item['name'],
        'datetimes': selected_item['datetimes'],
        'elevation': selected_item['elevation'],
        'code': selected_item['code'],
        'full_name': selected_item['full_name'],
        'short_name': selected_item['short_name'],
        'zone': selected_item['zone'],
        'wereda': selected_item['wereda'],
        'kebele': selected_item['kebele'],
        'locality_n': selected_item['locality_n'],
        'organizati': selected_item['organizati'],
        'destinatio': selected_item['destinatio'],
        'status': selected_item['status'],
        'area_sqkm': selected_item['area_sqkm'],
        'yearly_est': selected_item['yearly_est'],
        'unesco_reg': selected_item['unesco_reg'],
        'descriptio': selected_item['descriptio'],
        'photo_no': selected_item['photo_no'],
        'photo_loca': selected_item['photo_loca'],
        'site_des_a': selected_item['site_des_a'],
        'amharic': selected_item['amharic'],
        'english': selected_item['english'],
        'x': selected_item['x'],
        'y': selected_item['y'],
        'image1': selected_item['image1'],
        'image2': selected_item['image2']
                   
                    })
            return JsonResponse(feature)
    else:
            return JsonResponse({"error": "No point found"}, status=404)
        
        
from django.db.models import Count
def app(request):
        # Assuming you have retrieved data from your models
    destinations = Destinations.objects.all()
    services = Services.objects.all()
    context['destinations_'] = destinations.values_list('full_name')
    context['services_'] = services.values_list('full_name')
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
    distinct_destinations = combined_data['destinations'].values('destinatio').annotate(count=Count('destinatio'))
    distinct_services = combined_data['services'].values('service_ty').annotate(count=Count('service_ty'))
    context['distinct_destinations'] = json.dumps(list(distinct_destinations))
    context['distinct_services'] = json.dumps(list(distinct_services))
    # context['boundary'] = json.dumps(list(getBoundary()))
    # print(getBoundary())
    return render(request,'main/index.html',context)





class DestinationsViewSet(viewsets.ModelViewSet):
    queryset = Destinations.objects.all()
    serializer_class = DestinationsSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer