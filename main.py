import secret
import vk_api


def friends_list(user):
    tools = vk_api.VkTools(vk_session)
    friends = tools.get_all('friends.get', 1, {'user_id': user, 'name_case': 'acc'})
    return friends['items']


def bfs(start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in friends_list(vertex):
            print(next)
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

# def bfs(start):
#     used, queue = set(), [start]
#     while queue:
#         u = queue.pop(0)
#         if u not in used:
#             used.add(u)
#             queue.extend(friends_list(u) - used)


vk_session = vk_api.VkApi(secret.login, secret.password)

try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)

id1 = 211709668
id2 = 83645740
print(shortest_path(id1, id2))
