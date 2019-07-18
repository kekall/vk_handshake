import requests
import json
import secret


def friends_list(user):
    request = requests.get(
        f'https://api.vk.com/method/friends.get?user_id={user}&&name_case=acc&v=5.101&access_token={secret.token}')
    friends = json.loads(request.text)
    try:
        return friends['response']['items']
    except:
        return []


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


id1 = 211709668
id2 = 83645740
print(shortest_path(id1, id2))


# def bfs(start, goal):
#     queue, used = [], []
#     path = {}
#     used.append(start)
#     queue.append(start)
#     while queue:
#         u = queue.pop(0)
#         for friend in friends_list(u):
#             if friend == goal:
#                 return path
#             if friend not in used:
#                 used.append(friend)
#                 queue.append(friend)
#                 path[friend] = u
