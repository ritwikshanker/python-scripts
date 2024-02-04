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


def check_following_back(followers, following):
    not_following_back = [user for user in following if user not in followers]
    return not_following_back


if __name__ == "__main__":
    followers_json = load_json("followers.json")
    following_json = load_json("following.json")["relationships_following"]

    followers = get_users(followers_json)
    following = get_users(following_json)

    not_following_back = check_following_back(followers, following)

    print("Users not following you back:")
    for user in not_following_back:
        print(user)
