# Real-time Urban Microclimate Monitoring System: A Comprehensive Overview

## Introduction
Climate change and rapid urbanization have led to a growing interest in understanding urban microclimates. This project aims to analyze the impact of green spaces on the urban microclimate by comparing microclimate data from green and non-green spaces.

## System Overview
The urban microclimate monitoring system consists of several components:
1. Data Collection
2. Data Ingestion
3. Data Storage
4. Data Processing
5. Data Visualization

The system leverages Python, Kafka, SQLite, and Docker to create a scalable, real-time data pipeline capable of handling both streaming and batch data.

## Data Collection
The data collection component fetches real-time microclimate data from various sources, including temperature, humidity, air quality data, and green space locations, which are obtained from Overpass API and OpenWeather API. Random non-green space coordinates are also generated using a custom Python function.

## Data Ingestion
This component processes and combines the fetched data into a unified format. The combined data is then sent to Kafka for real-time data ingestion and further processing.

## Data Storage
Kafka acts as an intermediate storage layer, allowing the system to handle both streaming and batch data. A Kafka consumer is implemented to store the microclimate data in a SQLite database.

## Data Processing
This component involves analyzing the microclimate data to draw insights into the impact of green spaces on the urban microclimate. This includes calculating average temperature, humidity, and air quality values for both green and non-green spaces.

## Data Visualization
A web application is developed using Flask to display the data on an interactive map, along with summary statistics and visualizations. This allows users to easily compare microclimate data between green and non-green spaces.

## Conclusion
The real-time urban microclimate monitoring system offers a comprehensive solution for understanding the impact of green spaces on urban microclimates. The system provides a scalable and flexible platform for collecting, processing, and analyzing microclimate data, proving invaluable for designing more sustainable and resilient cities.
