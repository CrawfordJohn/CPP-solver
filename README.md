# CPP-solver
CityStrides running route optimizer using Chinese Postman Problem Solver - my senior project

Steps for using:
1. Download QGIS if not already installed
2. Download all the python files found above and put in plugins file in QGIS. Usual path would be AppData -> Roaming -> QGIS -> QGIS3 -> profiles -> default -> python -> plugins, and create a new folder for the Chinese Postman plugin to input all the files
3. Download QuickOSM plugin from QGIS plugin extension (Plugins -> Manage and Install Plugins -> QuickOSM)
4. Find QuickOSM under Vector tab and open
5. Click Query tab on left and enter following query (CityStrides eligible streets). Change 'Town Name' and 'State Name' to area of interest:

[out:xml] [timeout:25];
{{geocodeArea:Town Name, State Name}} -> .area_0;
(
node["name"]["highway"]["highway"!="bridleway"]["highway"!="bus_guideway"]["highway"!="bus_stop"]["highway"!="construction"]["highway"!="cycleway"]     ["highway"!="elevator"]["highway"!="escape"]["highway"!="footway"]["highway"!="motorway"]["highway"!="motorway_junction"]["highway"!="motorway_link"]["highway"!="path"]["highway"!="platform"]["highway"!="raceway"]["highway"!="rest_area"]["highway"!="services"]["highway"!="steps"]["highway"!="track"]["highway"!="trunk"]["access"!="customers"]["access"!="no"]["access"!="private"]["public_transport"!="platform"](area.area_0);
way["name"]["highway"]["highway"!="bridleway"]["highway"!="bus_guideway"]["highway"!="bus_stop"]["highway"!="construction"]["highway"!="cycleway"]["highway"!="elevator"]["highway"!="escape"]["highway"!="footway"]["highway"!="motorway"]["highway"!="motorway_junction"]["highway"!="motorway_link"]["highway"!="path"]["highway"!="platform"]["highway"!="raceway"]["highway"!="rest_area"]["highway"!="services"]["highway"!="steps"]["highway"!="track"]["highway"!="trunk"]["access"!="customers"]["access"!="no"]["access"!="private"]["public_transport"!="platform"](area.area_0);
relation["name"]["highway"]["highway"!="bridleway"]["highway"!="bus_guideway"]["highway"!="bus_stop"]["highway"!="construction"]["highway"!="cycleway"]["highway"!="elevator"]["highway"!="escape"]["highway"!="footway"]["highway"!="motorway"]["highway"!="motorway_junction"]["highway"!="motorway_link"]["highway"!="path"]["highway"!="platform"]["highway"!="raceway"]["highway"!="rest_area"]["highway"!="services"]["highway"!="steps"]["highway"!="track"]["highway"!="trunk"]["access"!="customers"]["access"!="no"]["access"!="private"]["public_transport"!="platform"](area.area_0);
);
(._;>;);
out body;

6. Run Query and select line layer
7. Use 'explode lines' in the processing toolbox on the line layer
8. change project CRS to EPSG:5071 (if using for North America) or other meter-based CRS, and reproject the exploded line layer to the same CRS using the reproject lines tool in the processing toolbox
9. select area that you want to run the Chinese Postman Solver on with the select features by polygon tool, and draw a shape around the area of interest.
10. Go to plugins, and run the Chinese Postman Solver on the selected area
11. Optimal path and distance are outputted, path can be exported as a csv or gpx file to use elsewhere if wanted.


