import json
from datetime import datetime


def filter_objects(start_timestamp, end_timestamp=None):
    # Convert start timestamp to a datetime object
    start_date = datetime.strptime(start_timestamp, "%Y-%m-%d")

    # If end timestamp is provided, convert it to datetime object, else use current time
    if end_timestamp:
        end_date = datetime.strptime(end_timestamp, "%Y-%m-%d")
    else:
        end_date = datetime.now()

    # List to hold the filtered objects
    filtered_objects = []

    # Open the JSON file
    with open('Records.json', 'r') as file:
        data = json.load(file)

        # Iterate through the objects within the "locations" key
        for obj in data['locations']:
            # Extract the date part of the timestamp
            date_str = obj['timestamp'].split("T")[0]
            # Convert the date string to a datetime object
            obj_date = datetime.strptime(date_str, "%Y-%m-%d")

            # Check if the object's date falls within the specified range
            if start_date <= obj_date <= end_date:
                filtered_objects.append(obj)

    return filtered_objects


# Example usage of the function
start_timestamp = "2023-07-21"
result = filter_objects(start_timestamp)

# Save the filtered objects to a new JSON file
with open('filtered_data.json', 'w') as file:
    json.dump({"locations": result}, file)

print("Filtered objects have been saved to filtered_data.json")
