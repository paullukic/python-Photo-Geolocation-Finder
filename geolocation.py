import exifread
import folium

# Open image file for reading (binary mode)
f = open("yourgpstaggedphoto.jpg", 'rb')

# Return Exif tags
tags = exifread.process_file(f, strict=True)


# function to convert degrees to decimals
def convert_to_degrees(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)


# get latitude
for tag in tags.keys():
    if tag in ('GPS GPSLatitude'):
        latitude = tags[tag]

# get longitude
for tag in tags.keys():
    if tag in ('GPS GPSLongitude'):
        longitude = tags[tag]

# create new variable from converted coordinates
latitudeD = convert_to_degrees(latitude)
longitudeD = convert_to_degrees(longitude)

# test
print(latitudeD, longitudeD)

# create new map with folium
map = folium.Map(location=[latitudeD, longitudeD], zoom_start=15)
featureG = folium.FeatureGroup(name="My Map")

# add marker
for coordinates in [[latitudeD, longitudeD]]:
    featureG.add_child(folium.Marker(location=coordinates, popup="Your Photo", icon=folium.Icon(color='red')))
map.add_child(featureG)

# save the map
map.save("Map1.html")
