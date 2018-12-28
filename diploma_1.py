import requests
from time import sleep
import json
import sys


def write_json(data):
    with open('ansver.json','w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def check_f(user, group):
    token = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
    params = {
    'group_id': group,
    'user_id': user,
    'count': 10,
    'offset': 0,
    'access_token': token,
    'v':'5.92',
    'extended': 0,
    'fields': 'contacts'
    }

    response = requests.get('https://api.vk.com/method/groups.isMember', params)
    #sleep(0.1)
    sys.stdout.write('|')
    sys.stdout.flush()
    return response.json()['response']

def search_friends(users, group):
    list_f = []
    if len(list_f) < 1:
        for user in users:
            a = check_f(user, group)
            if a == 1:
                list_f.append(user)

    if len(list_f) == 1:
        print('В {} группе ваших друзей нет'.format(group))
    else:
        return group


def main():
    ansver = []
    dict_json = []
    token = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
    params = {
        'access_token': token,
        'v':'5.92'
        }

    response = requests.get('https://api.vk.com/method/groups.get', params)
    list_groups = response.json()
    list_groups=list_groups['response']['items']
    response_2 = requests.get('https://api.vk.com/method/friends.get', params)
    list_friends = response_2.json()['response']['items']
    #b=list_friends[14:25]
    for group in list_groups:
        id_group = search_friends(list_friends, group)
        if id_group == None:
            pass
        else:
            ansver.append(id_group)

    for group in ansver:
        token = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
        params_a = {
        'group_id': str(group) ,
        'count': 100,
        'offset': 0,
        'access_token': token,
        'v':'5.92',
        'extended': 0,
        'fields': 'contacts'
        }
        response1 = requests.get('https://api.vk.com/method/groups.getById', params_a)
        name_group = response1.json()['response'][0]['name']
        gid_group = response1.json()['response'][0]['id']
        response = requests.get('https://api.vk.com/method/groups.getMembers', params_a)
        count = response.json()['response']['count']
        dict_json.append({'name': name_group, 'gid': gid_group, 'members_count': count })

    write_json(dict_json)

if __name__ == '__main__':
    main()
