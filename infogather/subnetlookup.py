import requests

def subnet_lookup(cidr):
    try:
        url = f'https://api.hackertarget.com/subnetcalc/?q={cidr}'
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()  # Parse the JSON response

        # Now you can work with the 'data' dictionary
        print(data)
        
    except requests.RequestException as e:
        print(f"Error making the request: {e}")
    except ValueError as ve:
        print(f"Error parsing JSON: {ve}")


