import json


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def get_users(json_data):
    users = []
    for entry in json_data:
        user_data = entry.get("string_list_data", [])
        if user_data:
            for user_entry in user_data:
                users.append(user_entry["value"])
    return users

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)


def check_following_back(followers, following):
    not_following_back = [user for user in following if user not in followers]
    me_not_following_back = [user for user in followers if user not in following]
    return not_following_back, me_not_following_back


if __name__ == "__main__":
    followers_json = load_json("followers.json")
    following_json = load_json("following.json")["relationships_following"]

    followers = get_users(followers_json)
    print("Total Number of Followers : " + str(len(followers)))
    following = get_users(following_json)
    print("Total Number of Following : " + str(len(following)))
    not_following_back, me_not_following_back = check_following_back(followers, following)
    print("Total Number of People not Following back : " + str(len(not_following_back)))
    print("Users not following you back:")
    for user in not_following_back:
        print(link('https://instagram.com/' + user + "/", user))
    print("\nTotal Number of People I'm not following back : " + str(len(me_not_following_back)))
    print("Users whom you are not following back:")
    for user in me_not_following_back:
        print(link('https://instagram.com/' + user + "/", user))

