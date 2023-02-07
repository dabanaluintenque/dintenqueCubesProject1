
# author: Dabana Intenque
import sys

import requests

from secret import wufooKey
from requests.auth import HTTPBasicAuth


def get_wufoo_data() -> dict:
    url = "https://dintenque.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"

    response = requests.get(url, auth=HTTPBasicAuth(wufooKey, 'pass'))
    if response.status_code != 200:  # if we don't get an ok there is a trouble
        print(f"Failed to get data, response code:{response.status_code} and error message:{response.reason}")

        sys.exit(-1)

    json_response = response.json()
    # add comment to test workflow
    # json response will be either a dictionary or a list of dictionaries each dictionary represents a json object
    return json_response


def get_wufoo_entries(entries):
    values = get_wufoo_data()
    for key, val in values.items():
        for item in val:
            print(item)


def print_wufoo_data():
    data = get_wufoo_data()
    print(get_wufoo_entries(data))


if __name__ == '__main__':
    with open('data.txt', 'a') as f:
        values = get_wufoo_data()
        for key, val in values.items():
            for item in val:
                f.write('\n')
                f.write(str(item))
