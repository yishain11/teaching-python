import requests

GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

API_KEY = "531e8f3396716ad8772d853096e728ac"


def get_location(city, country, state=""):
    if country == "US" and state:
        location_query = f"{city},{state},{country}"
    else:
        location_query = f"{city},{country}"

    params = {"q": location_query, "limit": 1, "appid": API_KEY}

    response = requests.get(GEO_URL, params=params, timeout=10)

    response.raise_for_status()

    locations = response.json()

    if not locations:
        return None

    return locations[0]


def get_weather(latitude, longitude):
    params = {"lat": latitude, "lon": longitude, "appid": API_KEY, "units": "metric"}

    response = requests.get(WEATHER_URL, params=params, timeout=10)

    response.raise_for_status()

    return response.json()


def print_weather(location, weather):
    city = location["name"]
    country = location["country"]
    state = location.get("state")

    temperature = weather["main"]["temp"]
    feels_like = weather["main"]["feels_like"]
    humidity = weather["main"]["humidity"]
    condition = weather["weather"][0]["description"]
    wind_speed = weather["wind"]["speed"]

    print()
    print(f"City: {city}")

    if state:
        print(f"State/Region: {state}")

    print(f"Country: {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")


def main():
    city = input("Enter city: ").strip()
    country = input("Enter two-letter country code: ").strip().upper()

    if not city or not country:
        print("City and country cannot be empty.")
        return

    if len(country) != 2:
        print("Country code must contain two letters.")
        return

    state = ""

    if country == "US":
        state = input("Enter two-letter state code: ").strip().upper()

        if len(state) != 2:
            print("State code must contain two letters.")
            return

    try:
        location = get_location(city, country, state)

        if location is None:
            print("Location not found.")
            return

        weather = get_weather(location["lat"], location["lon"])

        print_weather(location, weather)

    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code

        if status_code == 401:
            print("Invalid API key.")
        else:
            print(f"HTTP error: {status_code}")

    except requests.exceptions.Timeout:
        print("The request timed out.")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the weather service.")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    except (KeyError, IndexError, TypeError, ValueError):
        print("The API response did not contain the expected data.")


if __name__ == "__main__":
    main()
