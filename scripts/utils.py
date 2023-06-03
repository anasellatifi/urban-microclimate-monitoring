import random

def generate_random_coordinates(bbox, num_points):
    lat_min, lon_min, lat_max, lon_max = map(float, bbox.split(","))
    random_coordinates = []

    for _ in range(num_points):
        lat = random.uniform(lat_min, lat_max)
        lon = random.uniform(lon_min, lon_max)
        random_coordinates.append({"lat": lat, "lon": lon})

