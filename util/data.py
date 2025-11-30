import requests

def get_api_data(url):
    response = requests.get(url)
    data = response.json()
    return data


def validate_float(n):    
    try:
        return float(n)
    except (TypeError, ValueError, Exception):
        return 0
    
def validate_int(n):
    try:
        return int(n)
    except (TypeError, ValueError, Exception):
        return 0