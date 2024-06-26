# Django Proxy API Server

## Overview

This Django application serves as an intermediary for fetching sunrise and sunset times for a given city by querying external APIs. The application demonstrates how to integrate third-party APIs into a Django project, effectively acting as a simple proxy for retrieving geolocation and sunrise/sunset data.

## Features

- Fetches geolocation (latitude and longitude) for a specified city and country using the API Ninjas Geocoding API.
- Retrieves sunrise and sunset times for the obtained coordinates using the Sunrise-Sunset.io API.
- Responds with the original request parameters along with the sunrise and sunset times in JSON format.

## APIs Used

### 1. API Ninjas Geocoding API
- **Endpoint**: `https://api.api-ninjas.com/v1/geocoding`
- **Request Type**: `GET`
- **Parameters**:
  - `city`: Name of the city (e.g., `London`)
  - `country`: Name of the country (e.g., `England`)
- **Headers**:
  - `X-Api-Key`: API key required for authentication

### 2. Sunrise-Sunset.io API
- **Endpoint**: `https://api.sunrisesunset.io/json`
- **Request Type**: `GET`
- **Parameters**:
  - `lat`: Latitude of the location
  - `lng`: Longitude of the location

## to user this server




- `1. Clone this repository.`
- `2. get into the project directory.`  ```cd sunset_sunrise```
- `3. install required packages ` / ```pip install -r requirements.txt```
- `4. handle migrations`
- `5.` run ```python manage.py runserver```
- `6` `make GET requests at` http://127.0.0.1:8000/ (default) `with the request body provided below`
#### request body:
```

{
    "city":"your city name goes here",
    "country":"your country name goes here"
}
```