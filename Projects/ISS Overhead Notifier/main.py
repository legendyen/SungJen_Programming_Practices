import re
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# if re.search('^4.', str(response.status_code)):
#     raise Exception("The page you are looking does not exist.")
# elif re.search('^5.', str(response.status_code)):
#     raise Exception("The website you are looking is in error.")

response.raise_for_status()

data = response.json()
# print(data)

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

print("Current ISS position")
print("Longitude:", longitude)
print("Latitude:", latitude)
