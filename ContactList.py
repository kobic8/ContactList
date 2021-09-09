import json


def search_bf(txt, pat):
    """ Bruteforce search of pattern in a given string """
    len_pat = len(pat)
    ind = 0
    for ch in txt[:]:
        if ch != pat[ind]:
            ind = 0
        else:
            if ind == len_pat - 1:  # the whole pattern was scanned and found in txt
                return True
            else:
                ind += 1
    return False


def main():
    """ The program loads a contact list as a json file (dict_to_json.json), asks from the user names to locate and
    retrieves the matched contacts """

    filename = "dict_to_json.json"
    with open(filename) as f:
        all_contacts = json.load(f)
    print(all_contacts.keys())

    user_input = input("Enter something:")
    while not user_input.lower() == 'q':
        if type(user_input) == int:  # we iterate through values
            user_input = str(user_input)

        matched = {}
        for key, value in all_contacts.items():
            if search_bf(key.lower(), user_input.lower()) or search_bf(value, user_input):
                matched[key] = value

        print("The following contacts found matched:\n {}".format(matched))
        user_input = input("Find another contact, or refine the search. Press q to exit:")
    print("Thank you")


if __name__ == '__main__':
    main()
