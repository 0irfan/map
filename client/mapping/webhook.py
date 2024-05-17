import requests
import database
import json

def handle_podio_webhook(data):
    # Pretty print the JSON data
    print("Received webhook data:")
    print(json.dumps(data, indent=4))

    # Extract relevant information from the data dictionary
    if 'type' in data and data['type'] == 'Item':
        item = data.get('item', {})
        external_id = item.get('external_id')
        latitude = item.get('fields', {}).get('location', {}).get('latitude')
        longitude = item.get('fields', {}).get('location', {}).get('longitude')
        title = item.get('fields', {}).get('title', {}).get('value')
        url = item.get('app_url')

        # Check if essential data is present
        if external_id is not None and latitude is not None and longitude is not None and title is not None and url is not None:
            # Assuming database.add_item() method adds the item to the database
            # Ensure that your database interaction code is implemented correctly
            database.add_item(external_id, latitude, longitude, title, url)
        else:
            print("Some essential data is missing. Skipping database insertion.")
    else:
        print("Data does not contain 'type' or 'type' is not 'Item'. Skipping database insertion.")

    # Additional processing for other types of webhook data if needed

# Pretty print the JSON data



    # Additional processing for other types of webhook data if needed
