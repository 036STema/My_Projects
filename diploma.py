from urllib.parse import urlencode
import requests
import progressbar
import time

token = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'

params = {
    'access_token': token,
    #'group_id':'142410745',
    'v':'5.92'
}

response = requests.get('https://api.vk.com/method/groups.get', params)
list_groups = response.json()
list_groups=list_groups['response']['items']
print(list_groups)
response_2 = requests.get('https://api.vk.com/method/friends.get', params)
list_friends = response_2.json()
list_friends=list_friends['response']['items']
ansver = []

def main(user, group):
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
    #time.sleep(0.1)
    return response.json()

def search_friends(users, group):
    list_f = []
    if len(list_f) < 1:
        for user in users:
            a= main(user, group)
            if a == 1:
                list_f.append(user)

    print(list_f)
    if len(list_f) == 0:
        print('В {} группе ваших друзей нет'.format(group))
        ansver.append(group)

for group in list_groups:
    search_friends(list_friends, group)

for x in ansver:
    params_a = {
    'group_id': str(x) ,
    'count': 10,
    'offset': 0,
    'access_token': token,
    'v':'5.92',
    'extended': 0,
    'fields': 'contacts'
    }
    response4 = requests.get('https://api.vk.com/method/groups.getById', params_a)
print(response4.json()['response'][0]['name'])


