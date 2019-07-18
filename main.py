import requests
import json
import secret


def friends_list(user):
    request = requests.get(
        f'https://api.vk.com/method/friends.get?user_id={user}&v=5.101&access_token={secret.token}')
    friends = json.loads(request.text)
    try:
        return friends['response']['items']
    except:
        return []


def get_user(user):
    request = requests.get(
        f'https://api.vk.com/method/users.get?user_ids={user}&&name_case=acc&v=5.101&access_token={secret.token}')
    user_info = json.loads(request.text)
    try:
        return user_info['response'][0]
    except:
        return 'error'


def bfs(start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in friends_list(vertex):
            if next not in set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))


def shortest_path(start, goal):
    try:
        return next(bfs(start, goal))
    except StopIteration:
        return None


user1 = input()
user2 = input()

path = shortest_path(get_user(user1)['id'], get_user(user2)['id'])[1:-1]
print('Вы знакомы через: ')
for id in path:
    id = int(id)
    print(f'{get_user(id)["first_name"]} {get_user(id)["last_name"]}')
