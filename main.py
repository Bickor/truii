import requests
import os
import secrets

myKey = secrets.TRELLO_KEY
myToken = secrets.TRELLO_TOKEN
url_member = "https://api.trello.com/1/members/me/boards?key=" + myKey + "&token=" + myToken # All member information
url_boards = "https://api.trello.com/1/members/me/boards?fields=name,url&key=" + myKey + "&token=" + myToken # Get all board names

def main():
    print("Hello World!")
    # print(url)
    # response = requests.get(url_member)
    # print(response.json())

    response = requests.get(url_boards)
    print("Response done")
    print(response.status_code)
    if (response.status_code < 300):
        print(response.json())
    else:
        print("Request failed")

    # print(myKey)
    # print(myToken)





main()