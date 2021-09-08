import json

filename = "dict_to_json.json"
with open(filename) as f:
        all_contacts = json.load(f)
print(all_contacts.keys())

user_input = input("Enter something:")

if type(user_input) == int:  # we iterate through values
    user_input = str(user_input)

matched = {}
for key, value in all_contacts.items():
    if user_input.lower() in key.lower() or user_input in value:
        matched[key] = value

print("The following contacts found matched:\n {}".format(matched))