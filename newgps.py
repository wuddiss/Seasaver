from geopy.distance import geodesic

# Function to convert cylindrical coordinates to longitude and latitude
def cylindrical_to_lat_long(start_lat, start_lon, degrees, distance):
    # Convert cylindrical coordinates to latitude and longitude
    center_point = (start_lat, start_lon)  # Using the specified starting latitude and longitude as the center

    # Calculate destination point using geodesic
    destination_point = geodesic(kilometers=distance).destination(center_point, degrees)

    return destination_point.latitude, destination_point.longitude

# Example starting point coordinates change for use with sonar code.
start_latitude = 64.15182 # Example latitude
start_longitude = -21.93263  # Example longitude
start_heading = 360 #where the gps is heading in degrees
sonar_heading = 10 #where the sonar is pointing in degrees
sonar_distance = 10*10^(-3) #Distance to object in km IT HAS TO BE IN KM
new_heading = start_heading - sonar_heading

while True:
    if new_heading < 0:
        new_heading = new_heading + 360
    if new_heading < 360:
        new_heading = new_heading - 360
    else:
        return 
    
# Example cylindrical coordinates (degrees, distance in kilometers) change for use with sonar code
cylindrical_coords = (new_heading, sonar_distance)  

# Convert cylindrical coordinates to latitude and longitude
latitude, longitude = cylindrical_to_lat_long(start_latitude, start_longitude, *cylindrical_coords)

print(f"{latitude},{longitude}")
