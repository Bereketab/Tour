

const popupCloser = document.getElementById('popup-closer');

// Add a click event listener to the close button
popupCloser.addEventListener('click', function () {
    popup.getElement().style.display = 'none'; // Hide the popup
});


var geoserver_destination_url = "http://localhost:8088/geoserver/cms/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=cms%3Adestinations&maxFeatures=1000&outputFormat=application%2Fjson"
var geoserver_service_url = "http://localhost:8088/geoserver/GOTour/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=GOTour%3Aservices&maxFeatures=1000&outputFormat=application%2Fjson"

var services = {{ services| safe}}
var destinations = {{ destinations| safe}}

var map = new ol.Map({
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM(),
            name: 'OSM'
        })
    ],
    target: 'map-canvas',
    controls: ol.control.defaults({
        attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
            collapsible: false
        })
    }),
    view: new ol.View({
        center: [37, 8],
        zoom: 5,
        projection: 'EPSG:4326'
    })
});
var layerSwitcher = new ol.control.LayerSwitcher({
    tipLabel: 'Layer Switcher',
    reverse: true,
    groupSelectStyle: 'group'

});

map.addControl(layerSwitcher);

var jsonData = [
    {
        "text": "Services",
        "children": services
    },
    {
        "text": "Destinations",
        "children": destinations
    }
];
const iconMappings = {
'Services': 'bi-list', // Bootstrap 5 icon for "list"
'Air Port': 'bi-airport', // Bootstrap 5 icon for "airport"
'Bank': 'bi-bank', // Bootstrap 5 icon for "bank"
'Beverage': 'bi-cup-straw', // Bootstrap 5 icon for "cup-straw"
'Bus Terminal': 'bi-bus', // Bootstrap 5 icon for "bus"
'Café': 'bi-coffee', // Bootstrap 5 icon for "coffee"
'Camp Site': 'bi-tree', // Bootstrap 5 icon for "tree"
'Catholic Church': 'bi-church', // Bootstrap 5 icon for "church"
'Clinic': 'bi-hospital', // Bootstrap 5 icon for "hospital"
'College': 'bi-building', // Bootstrap 5 icon for "building"
'Garage': 'bi-tools', // Bootstrap 5 icon for "tools"
'Gas Station': 'bi-gas-pump', // Bootstrap 5 icon for "gas-pump"
'Health Center': 'bi-hospital', // Bootstrap 5 icon for "hospital"
'Health Post': 'bi-hospital', // Bootstrap 5 icon for "hospital"
'Hospital': 'bi-hospital', // Bootstrap 5 icon for "hospital"
'Hotel': 'bi-building', // Bootstrap 5 icon for "building"
'Lodge': 'bi-building', // Bootstrap 5 icon for "building"
'Mosque': 'bi-mosque', // Bootstrap 5 icon for "mosque"
'Municipal': 'bi-building', // Bootstrap 5 icon for "building"
'Museum': 'bi-museum', // Bootstrap 5 icon for "museum"
'Office': 'bi-building', // Bootstrap 5 icon for "building"
'Open Market': 'bi-shop', // Bootstrap 5 icon for "shop"
'Orthodox Church': 'bi-church', // Bootstrap 5 icon for "church"
'Pension': 'bi-building', // Bootstrap 5 icon for "building"
'Pharmacy': 'bi-flask', // Bootstrap 5 icon for "flask"
'Police Station': 'bi-shield', // Bootstrap 5 icon for "shield"
'Protestant Church': 'bi-church', // Bootstrap 5 icon for "church"
'Repair': 'bi-tools', // Bootstrap 5 icon for "tools"
'Restaurant': 'bi-restaurant', // Bootstrap 5 icon for "restaurant"
'School': 'bi-building', // Bootstrap 5 icon for "building"
'Stadium': 'bi-stadium', // Bootstrap 5 icon for "stadium"
'Supper Market': 'bi-cart', // Bootstrap 5 icon for "cart"
'University': 'bi-building', // Bootstrap 5 icon for "building"
'Destinations': 'bi-list', // Bootstrap 5 icon for "list"
'Cultural': 'bi-building', // Bootstrap 5 icon for "building"
'Man Made': 'bi-building', // Bootstrap 5 icon for "building"
'Natural': 'bi-tree' // Bootstrap 5 icon for "tree"
};


function buildTree($parent, data) {
$.each(data, function (index, item) {
var $li = $("<li></li>");
var $checkbox = $("<input type='checkbox' class='node-checkbox'>");
var $a = $("<a>" + item.text + "</a>");

if (item.children && item.children.length > 0) {
    console.log(item)
    $li.append($checkbox);
    $li.append($a);
    var $ul = $("<ul></ul>");
    $li.append($ul);
    buildTree($ul, item.children);
    $a.prepend("<span class='bi bi-chevron-right'></span>");
    if (iconMappings[item.text]) {
        console.log(iconMappings[item.text])
    $a.append("<span class='" + iconMappings[item.text] + "'></span>");
}
    $a.append("<span class='badge bg-primary'>"+item.children.length+"</span>"); 
} else {
    $li.append($checkbox);
    $li.append($a);
    // $a.append("<span class='bi bi-0-circle'></span>"); // Add the icon here
}

$parent.append($li);
});
}


function getCheckedHierarchy() {
    var hierarchy = {};

    function traverse(node, obj) {
        var text = node.text();
        obj[text] = {};
        node.siblings("ul").children("li").each(function () {
            var checkbox = $(this).children(".node-checkbox");
            if (checkbox.prop("checked")) {
                traverse($(this).children("a"), obj[text]);
            }
        });
    }

    $("#treeview > li").each(function () {
        var checkbox = $(this).children(".node-checkbox");
        if (checkbox.prop("checked")) {
            traverse($(this).children("a"), hierarchy);
        }
    });

    return hierarchy;
}

function updateOutput() {
    var hierarchy = getCheckedHierarchy();
    $("#output").text(JSON.stringify(hierarchy, null, 2));

    // Handle leaf nodes
    $("#treeview > li").each(function () {
        var $parentLi = $(this);
        var $checkboxes = $parentLi.find(".node-checkbox");
        var isChecked = $checkboxes.filter(":checked").length === $checkboxes.length;
        $parentLi.children(".node-checkbox").prop("checked", isChecked);
        if (isChecked && $parentLi.find("ul").length === 0) {
            var text = $parentLi.find("a").text();
            var parentText = $parentLi.parent().closest("li").find("a").text();
            if (!hierarchy[parentText]) {
                hierarchy[parentText] = [];
            }
            hierarchy[parentText].push(text);
        }
    });
    var checkedCheckboxes = getLeafNodeValues();
    updateMap(checkedCheckboxes)
}
async function fetchDestinationData() {
    try {
        const response = await fetch(geoserver_destination_url);
        const data = await response.json();
        return data.features || [];
    } catch (error) {
        console.error("Error fetching destination data:", error);
        return [];
    }
}

async function fetchServiceData() {
    try {
        const response = await fetch(geoserver_service_url);
        const data = await response.json();
        return data.features || [];
    } catch (error) {
        console.error("Error fetching service data:", error);
        return [];
    }
}
const markerIcon = new ol.style.Icon({
    src: '{% static "images/marker-icon.png"%}', // Replace with the path to your marker image
    anchor: [0.5, 1], // Center the icon on the feature's coordinates
    scale: 0.5, // Adjust the scale as needed
});
function createMarkerStyle(feature) {
    return new ol.style.Style({
        image: markerIcon,
    });
}

async function addFeaturesToVectorSource(vectorSource, data, checkedCheckboxes) {
    data.forEach(function (destinationFeature) {
        const splitId = destinationFeature.id.split('.');
        const isDestinations = splitId[0] === 'destinations';
        const full_name = isDestinations
            ? destinationFeature.properties.Full_Name
            : destinationFeature.properties.full_name;
        const wereda = isDestinations
            ? destinationFeature.properties.Wereda
            : destinationFeature.properties.wereda;

        if (checkedCheckboxes.includes(full_name)) {
            const coordinates = isDestinations
                ? destinationFeature.geometry.coordinates
                : destinationFeature.geometry.coordinates[0];

            const feature = new ol.Feature({
                geometry: new ol.geom.Point([coordinates[0], coordinates[1]]),
                name: full_name,
                wereda: wereda

            });

            // Set the marker style for the feature
            feature.setStyle(createMarkerStyle(feature));

            vectorSource.addFeature(feature);
        }
    });
}

async function updateMap(checkedCheckboxes, padding = 0) {
    const vectorSource = new ol.source.Vector(); // Create an empty vector source

    const vectorLayer = new ol.layer.Vector({
        source: vectorSource
    });

    map.getLayers().forEach(function (layer) {
        if (layer instanceof ol.layer.Vector) {
            map.removeLayer(layer);
        }
    });

    const destinationData = await fetchDestinationData();
    addFeaturesToVectorSource(vectorSource, destinationData, checkedCheckboxes);
    const serviceData = await fetchServiceData();
    addFeaturesToVectorSource(vectorSource, serviceData, checkedCheckboxes);

    // Calculate the extent of all features in the vector source
    const extent = vectorSource.getExtent();

    // Add padding to the extent
    const paddedExtent = ol.extent.buffer(extent, padding);

    // Animate the map view to the padded extent
    map.getView().fit(paddedExtent, map.getSize(), { duration: 1500 });

    map.addLayer(vectorLayer);
}


$(document).ready(function () {
    buildTree($("#treeview"), jsonData);
    $("#treeview ul").hide();

    $("#treeview a").click(function (e) {
        e.preventDefault();
        // Find the associated ul element and toggle its visibility
        var $ul = $(this).siblings("ul");
        $ul.toggle();

        // Toggle the bi-chevron-right and bi-chevron-down classes
        var $icon = $(this).find("span.bi");
        if ($icon.hasClass("bi-chevron-right")) {
            $icon.removeClass("bi-chevron-right").addClass("bi-chevron-down");
        } else {
            $icon.removeClass("bi-chevron-down").addClass("bi-chevron-right");
        }
    });
    $("#treeview .node-checkbox").change(function () {
        var isChecked = $(this).prop("checked");
        var $parentLi = $(this).closest("li");
        $parentLi.find(".node-checkbox").prop("checked", isChecked);
        updateOutput();

    });

    $("#treeview ul").hide();
});
function getLeafNodeValues() {
    var leafNodeValues = [];
    $("#treeview .node-checkbox:checked").each(function () {
        var $parentLi = $(this).closest("li");
        if ($parentLi.children("ul").length === 0) {
            leafNodeValues.push($(this).next("a").text()); // Store the label text of the checked leaf node
        }
    });
    return leafNodeValues;
}
const popup = new ol.Overlay({
    element: document.getElementById('popup'),
    positioning: 'bottom-center',
    stopEvent: false,
    offset: [0, -10], // Offset the popup slightly above the clicked point
});
map.addOverlay(popup);
function displayFeatureInfo(coordinate, content) {
    popup.setPosition(coordinate);
    document.getElementById('popup-content').innerHTML = content;
    popup.getElement().style.display = 'block';
}
map.on('click', function (event) {
    map.forEachFeatureAtPixel(event.pixel, function (feature) {
        // Get the feature's properties or any data you want to display
        const properties = feature.getProperties();
        console.log(properties)
        // Format the feature data for display in the popup
        const content = `
    <h3>${properties.name}</h3>
    <p>Other information: ${properties.wereda}</p>
    <!-- Add more properties here as need->ed -
`;

        // Display the feature data in the popup
        displayFeatureInfo(event.coordinate, content);
    });
});


