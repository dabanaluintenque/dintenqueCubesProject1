# author: Dabana Intenque
import sys

import cursor
import requests
# importing the Api wufoo_key from secret.py file
from secret import wufooKey
# importing the HTTPBasicAuth from the requests.auth package
from requests.auth import HTTPBasicAuth

# Database
from database import getDatabase


def get_wufoo_data() -> dict:
    # url link of the wufoo form
    url = "https://dintenque.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"
    # requesting the wufoo form from the url
    response = requests.get(url, auth=HTTPBasicAuth(wufooKey, 'pass'))
    if response.status_code != 200:  # if we don't get an ok there is a trouble
        print(f"Failed to get data, response code:{response.status_code} and error message:{response.reason}")
        # quit and stop the execution
        sys.exit(-1)

    # otherwise convert the data in a json format
    json_response = response.json()

    # json response will be either a dictionary or a list

    # add comment to test workflow
    # json response will be either a dictionary or a list of dictionaries each dictionary represents a json object
    return json_response


def get_wufoo_entries(data_entries: list, file_save=None):
    for entry in data_entries:
        for key, value in entry.items():
            print(f"{key}: {value}", file=file_save)
            print("***********************\n_____________________________",
                  file=file_save)


def main():
    # return the data from the get_wufoo_data function
    data = get_wufoo_data()
    # initialize the data entries
    data1 = data['Entries']
    # save as a .txt file format with 'w' (write)
    file_to_save = open("dates.txt", 'w')
    get_wufoo_entries(data1, file_save=file_to_save)


if __name__ == '__main__':
    main()
    getDatabase()
