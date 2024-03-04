var pointLayer; // Declare pointLayer outside the select event handler to maintain reference
  $("#autocomplete-input").autocomplete({
    source: availableTags,
    select: function(event, ui) {
        // Clear previous pointLayer if exists
        if (pointLayer) {
            map.removeLayer(pointLayer);
        }
console.log(ui.item)
        // Get the selected item data
        var selectedItem = ui.item;

// Check if x and y coordinates exist
if (selectedItem.hasOwnProperty('x') && selectedItem.hasOwnProperty('y')) {
    var pointFeature = new ol.Feature();

    if(selectedItem.whattype=="services"){
        
pointFeature.setGeometry(new ol.geom.Point([selectedItem.x, selectedItem.y]));
pointFeature.set('whattype', 'services');
pointFeature.set('geom', selectedItem.geom);
pointFeature.set('objectid', selectedItem.objectid);
pointFeature.set('x', selectedItem.x);
pointFeature.set('y', selectedItem.y);
pointFeature.set('z', selectedItem.z);
pointFeature.set('code', selectedItem.code);
pointFeature.set('full_name', selectedItem.full_name);
pointFeature.set('short_name', selectedItem.short_name);
pointFeature.set('zone', selectedItem.zone);
pointFeature.set('wereda', selectedItem.wereda);
pointFeature.set('kebele', selectedItem.kebele);
pointFeature.set('phone_line', selectedItem.phone_line);
pointFeature.set('email', selectedItem.email);
pointFeature.set('website', selectedItem.website);
pointFeature.set('service_ty', selectedItem.service_ty);
pointFeature.set('owner_name', selectedItem.owner_name);
pointFeature.set('moto', selectedItem.moto);

   
  
    }
    if(selectedItem.whattype=="destinations"){
        
pointFeature.setGeometry(new ol.geom.Point([selectedItem.x, selectedItem.y]));
pointFeature.set('whattype', 'destinations');
pointFeature.set('geom', selectedItem.geom);
pointFeature.set('objectid', selectedItem.objectid);
pointFeature.set('name', selectedItem.name);
pointFeature.set('datetimes', selectedItem.datetimes);
pointFeature.set('elevation', selectedItem.elevation);
pointFeature.set('code', selectedItem.code);
pointFeature.set('full_name', selectedItem.full_name);
pointFeature.set('short_name', selectedItem.short_name);
pointFeature.set('zone', selectedItem.zone);
pointFeature.set('wereda', selectedItem.wereda);
pointFeature.set('kebele', selectedItem.kebele);
pointFeature.set('locality_n', selectedItem.locality_n);
pointFeature.set('organizati', selectedItem.organizati);
pointFeature.set('destinatio', selectedItem.destinatio);
pointFeature.set('status', selectedItem.status);
pointFeature.set('area_sqkm', selectedItem.area_sqkm);
pointFeature.set('yearly_est', selectedItem.yearly_est);
pointFeature.set('unesco_reg', selectedItem.unesco_reg);
pointFeature.set('descriptio', selectedItem.descriptio);
pointFeature.set('photo_no', selectedItem.photo_no);
pointFeature.set('photo_loca', selectedItem.photo_loca);
pointFeature.set('site_des_a', selectedItem.site_des_a);
pointFeature.set('amharic', selectedItem.amharic);
pointFeature.set('english', selectedItem.english);
pointFeature.set('x', selectedItem.x);
pointFeature.set('y', selectedItem.y);
pointFeature.set('image1', selectedItem.image1);
pointFeature.set('image2', selectedItem.image2);

    }
  

    // Create a vector layer to hold the point feature
    pointLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [pointFeature],
            
        }),
        style:new ol.style.Style({
            image: new ol.style.Circle({
                radius: 6,
                fill: new ol.style.Fill({color: "yellow"}),
                stroke: new ol.style.Stroke({color: "red", width: 2})
            })
        })
    });

    // Add the point layer to the map
    map.addLayer(pointLayer);

    // Get the current zoom level
    var currentZoom_ = map.getView().getZoom();

    // Set the center of the map to the selected point
    var center = [selectedItem.x, selectedItem.y];
    map.getView().animate({
        center: center,
        zoom: currentZoom_ + 2, // You can adjust the zoom level here
        duration: 1000 // Duration of the animation in milliseconds
    });

        } else {
            console.warn("Selected item doesn't have x and y coordinates");
        }
    }
});

$("#sourceLocation").autocomplete({
    source: availableTags,
    select: function(event, ui) {
        // Clear previous pointLayer if exists
        if (pointLayer) {
            map.removeLayer(pointLayer);
        }
console.log(ui.item)
        // Get the selected item data
        var selectedItem = ui.item;

// Check if x and y coordinates exist
if (selectedItem.hasOwnProperty('x') && selectedItem.hasOwnProperty('y')) {
    var pointFeature = new ol.Feature();

    if(selectedItem.whattype=="services"){
        
pointFeature.setGeometry(new ol.geom.Point([selectedItem.x, selectedItem.y]));
pointFeature.set('whattype', 'services');
pointFeature.set('geom', selectedItem.geom);
pointFeature.set('objectid', selectedItem.objectid);
pointFeature.set('x', selectedItem.x);
pointFeature.set('y', selectedItem.y);
pointFeature.set('z', selectedItem.z);
pointFeature.set('code', selectedItem.code);
pointFeature.set('full_name', selectedItem.full_name);
pointFeature.set('short_name', selectedItem.short_name);
pointFeature.set('zone', selectedItem.zone);
pointFeature.set('wereda', selectedItem.wereda);
pointFeature.set('kebele', selectedItem.kebele);
pointFeature.set('phone_line', selectedItem.phone_line);
pointFeature.set('email', selectedItem.email);
pointFeature.set('website', selectedItem.website);
pointFeature.set('service_ty', selectedItem.service_ty);
pointFeature.set('owner_name', selectedItem.owner_name);
pointFeature.set('moto', selectedItem.moto);

   
  
    }
    if(selectedItem.whattype=="destinations"){
        
pointFeature.setGeometry(new ol.geom.Point([selectedItem.x, selectedItem.y]));
pointFeature.set('whattype', 'destinations');
pointFeature.set('geom', selectedItem.geom);
pointFeature.set('objectid', selectedItem.objectid);
pointFeature.set('name', selectedItem.name);
pointFeature.set('datetimes', selectedItem.datetimes);
pointFeature.set('elevation', selectedItem.elevation);
pointFeature.set('code', selectedItem.code);
pointFeature.set('full_name', selectedItem.full_name);
pointFeature.set('short_name', selectedItem.short_name);
pointFeature.set('zone', selectedItem.zone);
pointFeature.set('wereda', selectedItem.wereda);
pointFeature.set('kebele', selectedItem.kebele);
pointFeature.set('locality_n', selectedItem.locality_n);
pointFeature.set('organizati', selectedItem.organizati);
pointFeature.set('destinatio', selectedItem.destinatio);
pointFeature.set('status', selectedItem.status);
pointFeature.set('area_sqkm', selectedItem.area_sqkm);
pointFeature.set('yearly_est', selectedItem.yearly_est);
pointFeature.set('unesco_reg', selectedItem.unesco_reg);
pointFeature.set('descriptio', selectedItem.descriptio);
pointFeature.set('photo_no', selectedItem.photo_no);
pointFeature.set('photo_loca', selectedItem.photo_loca);
pointFeature.set('site_des_a', selectedItem.site_des_a);
pointFeature.set('amharic', selectedItem.amharic);
pointFeature.set('english', selectedItem.english);
pointFeature.set('x', selectedItem.x);
pointFeature.set('y', selectedItem.y);
pointFeature.set('image1', selectedItem.image1);
pointFeature.set('image2', selectedItem.image2);

    }
  

    // Create a vector layer to hold the point feature
    pointLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [pointFeature],
            
        }),
        style:new ol.style.Style({
            image: new ol.style.Circle({
                radius: 6,
                fill: new ol.style.Fill({color: "yellow"}),
                stroke: new ol.style.Stroke({color: "red", width: 2})
            })
        })
    });

    // Add the point layer to the map
    map.addLayer(pointLayer);

    // Get the current zoom level
    var currentZoom_ = map.getView().getZoom();

    // Set the center of the map to the selected point
    var center = [selectedItem.x, selectedItem.y];
    map.getView().animate({
        center: center,
        zoom: currentZoom_ + 2, // You can adjust the zoom level here
        duration: 1000 // Duration of the animation in milliseconds
    });

        } else {
            console.warn("Selected item doesn't have x and y coordinates");
        }
    }
});
