import requests
import random

def generate_random_coordinates(bbox, num_points):
    lat_min, lon_min, lat_max, lon_max = map(float, bbox.split(","))
    random_coordinates = []

    for _ in range(num_points):
        lat = random.uniform(lat_min, lat_max)
        lon = random.uniform(lon_min, lon_max)
        random_coordinates.append({"lat": lat, "lon": lon})

    return random_coordinates

def fetch_green_spaces_data(overpass_api_key, bbox, num_points=10):
    overpass_url = "https://overpass-api.de/api/interpreter"
    query = f"""
        [out:json];
        (node["leisure"="park"]({bbox});
         way["leisure"="park"]({bbox});
         relation["leisure"="park"]({bbox});
        );
        out center;
    """

    response = requests.get(overpass_url, params={"data": query})
    data = response.json()

    green_spaces_data = [
        {"id": i, "lat": element["lat"], "lon": element["lon"]}
        for i, element in enumerate(data["elements"])
    ]

    return green_spaces_data[:num_points]

def fetch_temperature_data(locations, open_weather_api_key):
    temperature_data = {}

    for location in locations:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "lat": location["lat"],
                "lon": location["lon"],
                "appid": open_weather_api_key,
                "units": "metric",
            },
        )
        data = response.json()
        temperature_data[location["id"]] = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
        }

    return temperature_data

def fetch_air_quality_data(locations, open_weather_api_key):
    air_quality_data = {}

    for location in locations:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/air_pollution",
            params={
                "lat": location["lat"],
                "lon": location["lon"],
                "appid": open_weather_api_key,
            },
        )
        data = response.json()
        air_quality_data[location["id"]] = {"aqi": data["list"][0]["main"]["aqi"]}

    return air_quality_data
