from folium import IFrame
import json
import folium

mapbox_access_token = "YOUR_MAPBOX_ACCESS_TOKEN_HERE"


def create_map(step=1, mapbox_access_token=mapbox_access_token, zoom_start=13.5):
    # Read the filtered data from the JSON file
    with open('filtered_data.json', 'r') as file:
        data = json.load(file)

    # Mapbox Streets style URL
    mapbox_url = f"https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{{z}}/{{x}}/{{y}}?access_token={mapbox_access_token}"

    # Create a base map using the specified Mapbox style
    mymap = folium.Map(location=[38.9968428, -77.0347021],
                       zoom_start=int(zoom_start), tiles=mapbox_url, attr='Mapbox')

    # Create a list to hold the coordinates for the PolyLine
    coordinates = []
    for i in range(0, len(data['locations']), step):
        location = data['locations'][i]
        latitude = location['latitudeE7'] / 1e7
        longitude = location['longitudeE7'] / 1e7
        coordinates.append([latitude, longitude])

    # Add the PolyLine to the map with a specific weight (thickness)
    folium.PolyLine(coordinates, color='blue', weight=2).add_to(mymap)

    # Add custom JavaScript to set the fractional zoom level
    fractional_zoom_script = f'<script>map.setZoom({zoom_start});</script>'
    iframe = IFrame(fractional_zoom_script, width=0, height=0)
    popup = folium.Popup(iframe, max_width=0)
    popup.add_to(mymap)

    # Save the map to an HTML file
    mymap.save('map.html')

    print(f"Map with line has been saved to map.html using Mapbox Streets.")


# Example usage:
create_map(step=2)
