import requests
import sys
import datetime
import time
import random


def print_location():
    text = (f'All right, We got some information about location '
            f'of International space station!\n'
            f'Longitude is {data["iss_position"]["longitude"]}\n'
            f'Latitude is {data["iss_position"]["latitude"]}\n')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.random() / 30)


base_url = 'http://api.open-notify.org/iss-now.json'


while True:
    response = requests.get(url=base_url)
    data = response.json()
    print_location()
    result = (f'{datetime.datetime.now()};'
              f'{data["iss_position"]["longitude"]};'
              f'{data["iss_position"]["latitude"]};\n')
    with open('Statistics/position.csv', 'a') as file:
        file.write(result)
    time.sleep(5)