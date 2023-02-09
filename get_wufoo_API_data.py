# author: Dabana Inteqque
import sys

import cursor
import requests
# importing the Api wufoo_key from secrets.py file
from secrets import wufooKey
# importing the HTTPBasicAuth from the requests.auth package
from requests.auth import HTTPBasicAuth


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
