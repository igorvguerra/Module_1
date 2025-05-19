import requests

url = "https://www.example.com"

response = requests.get(url)
print(f"HTTP request to {url} returned status {response.status_code}")