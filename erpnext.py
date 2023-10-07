import requests

# Define your API key
api_key = '031b2bd7255f167'

# Define the API endpoint for the "Housekeeping" DocType in your ERPNext instance
# Use 'site1.local' as the site name in the URL
api_url = 'http://127.0.0.1:8000/api/resource/Housekeeping/AGK_HS_101'

params = {
    'fields': ['name_housekeeping', 'housekeeping_id'],  # Specify the fields you want to retrieve
}
# Authentication headers
headers = {
    'Authorization': f'Bearer {api_key}',
}

try:
    # Make a GET request to retrieve data
    response = requests.get(api_url, headers=headers,params=params)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        data = response.json()
        # Process and use the data as needed
        print(data)
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")
