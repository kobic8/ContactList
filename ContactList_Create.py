import json
data = {"Joe Adams": "051669850",
        "Jane Smith": "055664147",
        "Brian Jovi": "074243432"
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
