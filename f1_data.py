from urllib.request import urlopen, URLError
from datetime import datetime
import json

# Use the correct session_key for the Chinese Grand Prix race
url = ('https://api.openf1.org/v1/car_data?driver_number=4&session_key=latest')


try:
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8'))

    if not data:
        print("No data has been found for car number 4 in the Chinese Grand Prix.")
    else:
        print(f"Found {len(data)} telemetry points for Lando Norris:")

        i = 0 
        for entry in data:
            timestamp = datetime.fromisoformat(entry['date'].replace('Z', '+00:00'))
            # Reformat to a readable format
            readable_time = timestamp.strftime('%B %d, %Y %H:%M:%S')
            print(f"Time: {readable_time}, Speed: {entry['speed']} km/h, RPM: {entry['rpm']}, Throttle: {entry['throttle']}% , Brake Pressed: {entry['brake']}, Gear: {entry['n_gear']}")
            i += 1

        print(f"The total number of rows of data display is: {i}")

except URLError as e:
    print(f"Failed to fetch data: {e}")
    