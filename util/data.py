import requests

def get_api_data(url):
    response = requests.get(url)
    data = response.json()
    return data