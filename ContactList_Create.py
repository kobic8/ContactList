import json
data = {"Kobi Cohen": "0536290656",
        "Bar Cohen": "0502564787",
        "Anat Dori": "0523755549",
        "David Marcovitz": "0546380204",
        "Omer Mintz": "0546966422",
        "David Weinstein": "0509077655"
        }

with open("dict_to_json.json", 'w') as fp:
    json.dump(data, fp)

# # pretty print the json into a file
# filename = "dict_to_json.json"
# with open(filename) as f:
#      all_contacts = json.load(f)

# readble_file = 'readble_contacts.json'
# with open(readble_file, 'w') as f:
#      json.dump(all_contacts, f, indent=4)
