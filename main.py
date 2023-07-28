import requests
import sys
import datetime
import time
import random


def print_location(data: dict) -> print:
    text = (f'All right, We got some information (time: {datetime.datetime.today()}) about location\n'
            f'of International space station!\n'
            f'Longitude is {data["iss_position"]["longitude"]}\n'
            f'Latitude is {data["iss_position"]["latitude"]}\n')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.random() / 30)


base_url = 'http://api.open-notify.org/iss-now.json'


def get_response() -> dict:
    response = requests.get(url=base_url)
    data = response.json()
    return data


def write_info(data) -> print:
    result = (f'{datetime.datetime.now()};'
              f'{data["iss_position"]["longitude"]};'
              f'{data["iss_position"]["latitude"]};\n')
    with open('Statistics/position.csv', 'a') as file:
        file.write(result)


while True:
    data = get_response()
    try:
        print_location(data)
    except KeyboardInterrupt:
        write_info(data)
        break
    write_info(data)
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        break
