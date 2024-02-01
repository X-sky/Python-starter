import os
import requests
import json

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data
response_dict = r.json()

# Create the directory if it doesn't exist
readable_file_path = "data_process/readable_hn_data.json"
os.makedirs(os.path.dirname(readable_file_path), exist_ok=True)
with open(readable_file_path, "w") as f:
    json.dump(response_dict, f, indent=4)
