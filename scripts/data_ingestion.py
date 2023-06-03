import os
import time
from data_fetcher import (
    fetch_green_spaces_data,
    fetch_temperature_data,
    fetch_air_quality_data,
    generate_random_coordinates,
)
from kafka_producer import create_kafka_producer, send_microclimate_data
from dotenv import load_dotenv

load_dotenv()

def main():
    topic = "microclimate_data"
    bootstrap_servers = ["localhost:9092"]
    producer = create_kafka_producer(bootstrap_servers)

    overpass_api_key = os.environ["OVERPASS_API_KEY"]
    open_weather_api_key = os.environ["OPEN_WEATHER_API_KEY"]
    bbox = os.environ["BOUNDING_BOX"]
    num_points = 10

    green_spaces_data = fetch_green_spaces_data(overpass_api_key, bbox, num_points)
    non_green_spaces_data = generate_random_coordinates(bbox, num_points)

    for point in non_green_spaces_data:
        point["id"] = len(green_spaces_data) + point["id"]

    all_locations = green_spaces_data + non_green_spaces_data

    while True:
        temperature_data = fetch_temperature_data(all_locations, open_weather_api_key)
        air_quality_data = fetch_air_quality_data(all_locations, open_weather_api_key)

        combined_data = []

        for location in all_locations:
            location_data = {
                "id": location["id"],
                "lat": location["lat"],
                "lon": location["lon"],
                "is_green_space": location["id"] < len(green_spaces_data),
            }
            location_data.update(temperature_data.get(location["id"], {}))
            location_data.update(air_quality_data.get(location["id"], {}))
            combined_data.append(location_data)

        send_microclimate_data(producer, topic, combined_data)
        time.sleep(60)  # Send data every minute

if __name__ == "__main__":
    main()
