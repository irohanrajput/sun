from django.http import JsonResponse
import requests


# fetching coordiates from apiNinjas
def getCoordinates(location):
    ninja_api_key = "eaMfoS5VActkeXwmF7ZlVA==DCNlLx5Jzpc15KUX" #exposed intentionally
    headers = {"X-Api-Key": ninja_api_key}
    geocodes = requests.get(
        "https://api.api-ninjas.com/v1/geocoding", headers=headers, params=location
    )

    geocodes = geocodes.json()[0]
    lattitude = geocodes["latitude"]
    longitude = geocodes["longitude"]
    return lattitude, longitude


# providing response using sunsetsunrise.io API
def getSunsetSunrise(request):
    if request.method == "GET":
        city = request.GET.get('city', 'new delhi')
        country = request.GET.get('country', "india")
        print(city)
        location = {"city": city, "country": country}
        lattitude, longitude = getCoordinates(location)
        base_url = "https://api.sunrisesunset.io"
        end_point = "/json"
        params = {"lat": lattitude, "lng": longitude}

        response = requests.get(f"{base_url}{end_point}", params=params)

        results = response.json()["results"]
        sunsetNsunrise = {
            f"sunrise in {location['city']}": results['sunrise'],
            f"sunset in {location['city']}": results['sunset']
            
        }
        return JsonResponse(sunsetNsunrise)
    else:
        return {request.method: "only GET requests allowed at this endpoint"}

#will work on error handeling later.