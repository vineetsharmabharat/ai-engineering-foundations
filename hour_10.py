import json
import urllib.request

print("--- Simulating Local JSON Parsing ---")
# 1. This represents raw text data arriving from an API
raw_api_response = '{"system": "Sentinel-Core", "uptime": 99.9, "active": true}'

# 2. We convert (load) the text string into a usable Python Dictionary
parsed_data = json.loads(raw_api_response)

print(f"System Name: {parsed_data['system']}")
print(f"Uptime: {parsed_data['uptime']}%")

print("\n--- Fetching Live Data from the Internet ---")
# 3. We reach out to a real, public API (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/users/1"

try:
    # Open the URL and read the response
    with urllib.request.urlopen(url) as response:
        live_data = response.read().decode('utf-8')
        
    # Parse the live internet text into a Python Dictionary
    user_profile = json.loads(live_data)
    
    print(f"Successfully retrieved data for: {user_profile['name']}")
    print(f"Company: {user_profile['company']['name']}")
    
except Exception as e:
    print(f"Network request failed: {e}")