import requests
import json
import simplejson as json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


endpoint_slug = "??? TO BE DEFINED ???"

# list_volunteers = requests.get(endpoint_slug).json()

list_volunteers = requests.get(endpoint_slug).json()

jprint(list_volunteers)

# Get data from API + create dictionary to avoid hitting API rate limit

volunteers_info = []
location_info = []

volunteer_dictionary = {}

for stream in list_volunteers:

    with open('locations_list.json', 'r') as locations:
        data = json.load(locations)

    data2 = next((sub['address'] for sub in data if sub['address'] == stream['Area where you can volunteer  พื้นที่ใกล้เคียงที่คุณสามารถเป็นอาสาสมัคร']), None) 
    jprint(data2)
    lat = next((sub['lat'] for sub in data if sub['address'] == stream['Area where you can volunteer  พื้นที่ใกล้เคียงที่คุณสามารถเป็นอาสาสมัคร']), None)
    jprint(lat)
    lng = next((sub['lng'] for sub in data if sub['address'] == stream['Area where you can volunteer  พื้นที่ใกล้เคียงที่คุณสามารถเป็นอาสาสมัคร']), None)
    jprint(lng)

    if stream['Area where you can volunteer  พื้นที่ใกล้เคียงที่คุณสามารถเป็นอาสาสมัคร'] == data2:
        volunteer_dictionary = {
            "content": str("<h3>"+stream['Name ชื่อ']+"</h3>"+"<p><b>🛺 Transportation: </b>"+stream["Transportation (car, motorbike) การเดินทาง (รถยนต์, มอเตอร์ไซด์)"]+"</p>"+"<p><b>✊ Help provided: </b>"+stream["How can you help?"]+"</p>"+"<p><b>📍 Area: </b>"+stream["Area where you can volunteer  พื้นที่ใกล้เคียงที่คุณสามารถเป็นอาสาสมัคร"]+"</p>"+"<p><b>📱 Contact details: </b>"+stream["Phone number /หมายเลขโทรศัพท์"]+"</p>"),
            # "Transportation": stream["Transportation"],
            # "Help": stream["Help"],
            "coordinates": {'lat': float(lat), 'lng':float(lng)},
            "car": str(stream['Car'])

        }
        jprint(volunteer_dictionary)
        volunteers_info.append(volunteer_dictionary)

    else:

        i = stream['Area where you can volunteer  พื้นที่ใกล้เคียงที่คุณสามารถเป็นอาสาสมัคร']

        endpoint_slug2 = f"https://maps.googleapis.com/maps/api/geocode/json?address={i}&key=???"

        list_locations = requests.get(endpoint_slug2).json()

        # Grab the first result

        if list_locations['results'] == []:
            print("API ERROR")
            continue
        else:

            list2 = list_locations['results'][0]
            
            locations_dictionary = dict()
            locations_dictionary['formatted address'] = list2['formatted_address']
            locations_dictionary['address'] = i
            locations_dictionary['lat'] = list2['geometry']['location']['lat']
            locations_dictionary['lng'] = list2['geometry']['location']['lng']
            
            locations_dictionary_copy = locations_dictionary.copy()

            location_info.append(locations_dictionary_copy)

            volunteer_dictionary = {
            "content": str("<h3>"+stream['Name ชื่อ']+"</h3>"+"<p><b>🛺 Transportation: </b>"+stream["Transportation (car, motorbike) การเดินทาง (รถยนต์, มอเตอร์ไซด์)"]+"</p>"+"<p><b>✊ Help provided: </b>"+stream["How can you help?"]+"</p>"+"<p><b>📍 Area: </b>"+stream["Area where you can volunteer  พื้นที่ใกล้เคียงที่คุณสามารถเป็นอาสาสมัคร"]+"</p>"+"<p><b>📱 Contact details: </b>"+stream["Phone number /หมายเลขโทรศัพท์"]+"</p>"),
                # "Transportation": stream["Transportation"],
                # "Help": stream["Help"],
                "coordinates": {'lat': float(list2['geometry']['location']['lat']), 'lng':float(list2['geometry']['location']['lng'])},
                "car": str(stream['Car'])
            }  

            volunteers_info.append(volunteer_dictionary)
    
jprint(location_info)
jprint(volunteers_info)

# Open existing dictionary and update
with open('locations_list.json', 'r') as fp:
    all_locations = json.load(fp)

    # jprint(all_locations)
    # jprint(location_info)

    all_locations.extend(location_info)

    with open('locations_list.json', 'w') as fp:
        json.dump(all_locations, fp)

# Update the list of volunteers (for final Javascript use after)
with open("covid_volunteers.json","w") as write_file:
    json.dump(volunteers_info, write_file)



    # if (stream["Lat"] == "#ERROR!" or stream["Lng"] == "#ERROR!" or stream["Lat"] == "#REF!" or stream["Lng"] == "#REF!"):
    #     continue
    # else:

# Create location dictionary

# i = "ลาดพร้าว-วังหิน, โชคชัย 4, รัชโยธิน"

# endpoint_slug2 = f"https://maps.googleapis.com/maps/api/geocode/json?address={i}&key=AIzaSyCR3lkg5YkTHl2pUhdwMCkg51-glwcZxbs"

# list_locations = requests.get(endpoint_slug2).json()['results']


# location_info = []

# locations_dictionary = {}
# for stream2 in list_locations:
#         locations_dictionary = {
#             "formatted address": stream2['formatted_address'],
#             "address": i,
#             "lat": stream2['geometry']['location']['lat'],
#             "lng": stream2['geometry']['location']['lng']
#     }
#         location_info.append(locations_dictionary)
#         jprint(locations_dictionary)

# jprint(location_info)

# with open('locations_list.json', 'w') as fp:
#     json.dump(locations_dictionary, fp)


# Places API URL
# "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={i}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyCR3lkg5YkTHl2pUhdwMCkg51-glwcZxbs"
