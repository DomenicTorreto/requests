import requests
import time


def questions(tag: str):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': round(time.time() - 172800),
              'todate': round(time.time()),
              'tagged': tag,
              'site': "stackoverflow"}
    response = requests.get(url, params=params)
    questions_list = [items_list['link'] for items_list in response.json()['items']]
    return questions_list


print(questions('Python'))
