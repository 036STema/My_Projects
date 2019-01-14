import requests
from time import sleep
import json
import sys

TOKEN = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
ID = '171691064'
VALUE = '' #eshmargunov


def get_response_api(url, params, token = TOKEN, number_of_attempts = 10):
  if 'access_token' not in params.keys():
      params['access_token'] = token
  for i in range(number_of_attempts):
    try:
      response = requests.get(url, params)
      response_json = response.json()
      print("От АПИ успешно получен ответ")
      return response_json['response']
    except KeyError:
      print("Не удалось получить ответ от АПИ, всего попыток: %s." % i)
      if 'error' in response_json.keys():
        print(response_json['error']['error_msg'])
      sleep(1)
  print("Не удалось получить ответ от АПИ, программа завершается.")
  sys.exit()


def write_json(data):
    with open('ansver.json','w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def check_f(user, group):
    params = {
    'group_id': group,
    'user_id': user,
    'access_token': TOKEN,
    'count': 10,
    'offset': 0,
    'v':'5.92',
    'extended': 0,
    'fields': 'contacts'
    }
    response = get_response_api('https://api.vk.com/method/groups.isMember', params)
    return response


def search_friends(users, group):
    list_f = []
    if len(list_f) < 1:
        for user in users:
            response = check_f(user, group)
            if response == 1:
                list_f.append(user)
    if len(list_f) >= 1:
        print('В {} группе есть ваши друзья'.format(group))
    else:
        return group


def main():
    answer = []
    dict_json = []
    params = {
        'value': VALUE,
        'user_id': ID,
        'v':'5.92'
        }
    list_groups = get_response_api('https://api.vk.com/method/groups.get', params)['items']
    list_friends = get_response_api('https://api.vk.com/method/friends.get', params)['items']
    #b=list_friends[14:25]
    for group in list_groups:
        id_group = search_friends(list_friends, group)
        if id_group == None:
            pass
        else:
            answer.append(id_group)
    for group in answer:
        params_a = {
        'group_id': str(group),
        'count': 100,
        'offset': 0,
        'v':'5.92',
        'extended': 0,
        'fields': 'contacts'
        }
        name_group = get_response_api('https://api.vk.com/method/groups.getById', params_a)[0]['name']
        gid_group = get_response_api('https://api.vk.com/method/groups.getById', params_a)[0]['id']
        count = get_response_api('https://api.vk.com/method/groups.getMembers', params_a)['count']
        dict_json.append({'name': name_group, 'gid': gid_group, 'members_count': count })
    write_json(dict_json)

if __name__ == '__main__':
    main()
