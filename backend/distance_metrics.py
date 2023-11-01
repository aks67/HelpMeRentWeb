import requests
import data_processing
import pandas as pd

access_token = 'pk.eyJ1IjoiYXhrNjcwIiwiYSI6ImNsbjVka2l5cTA2NTcycHF1MnFoNHh5bzgifQ.cSIgT6DWblr6rZMBPU4BWQ'

# Load existing travel times if the file exists, or create an empty DataFrame
try:
    travel_times_df = pd.read_csv('travel_times.csv')
except FileNotFoundError:
    travel_times_df = pd.DataFrame(columns=['Origin', 'Destination', 'TravelTime'])

def truncate_long(coord):
    return int(coord * 100) / 100.0

def get_dist(origin, dest):
    origin_coords = data_processing.get_coord(origin)
    if origin_coords is None:
        print(f"Invalid coordinates for origin: {origin}")
        return -1

    dest_coords = data_processing.get_coord(dest)
    if dest_coords is None:
        print(f"Invalid coordinates for destination: {dest}")
        return -1

    origin_long, origin_lat = truncate_long(origin_coords[0]), truncate_long(origin_coords[1])
    dest_long, dest_lat = truncate_long(dest_coords[0]), truncate_long(dest_coords[1])
    profile = 'driving-traffic'
    url = f'https://api.mapbox.com/directions/v5/mapbox/{profile}/{origin_long},{origin_lat};{dest_long},{dest_lat}?access_token={access_token}'

    travel_time_check = get_travel_time(origin, dest=dest)
    if travel_time_check == -1:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            travel_time = data['routes'][0]['duration']  # Travel time in seconds
            write_to_file(origin, dest, travel_time)
        else:
            print("Error in Request")
    else:
        return travel_time_check

'''
Store a CSV
'''
def write_to_file(origin, dest, travel_time):
    global travel_times_df  # Use the global DataFrame

    new_entry = {'Origin': origin, 'Destination': dest, 'TravelTime': travel_time}
    travel_times_df = pd.concat([travel_times_df, pd.DataFrame([new_entry])], ignore_index=True)

    # Save the updated DataFrame to a CSV file
    travel_times_df.to_csv('travel_times.csv', index=True)

def get_travel_time(origin, dest):
    try:
        matching_row = travel_times_df[(travel_times_df['Origin'] == origin) & (travel_times_df['Destination'] == dest)]
        if not matching_row.empty:
            return float(matching_row.iloc[0]['TravelTime'])
        else:
            return -1
    except FileNotFoundError:
        return -1

# Example usage:
if __name__ == '__main__':
    print(get_dist(origin=2033, dest=2016))

