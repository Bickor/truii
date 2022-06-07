import requests
import secrets

# Constants
myKey = secrets.TRELLO_KEY
myToken = secrets.TRELLO_TOKEN
member_id = secrets.MEMBER_ID

# URLs
url_boards = "https://api.trello.com/1/members/{}/boards".format(member_id) # Get information about all boards belonging to member_id

# Headers
headers = {
    "Accept": "application/json"
}

def getMemberBoardMetadata():
    print("Member information")

    # Add any fields needed to the query
    query = {
        "key": myKey,
        "token": myToken,
    }

    response = requests.request(
        "GET",
        url_boards,
        headers=headers,
        params=query
    )
    if (response.status_code < 300):
        print(response.json())
    else:
        print("Request failed")

def memberBoardsNames():
    query = {
        "key": myKey,
        "token": myToken,
        "fields": "name,url"
    }

    response = requests.request(
        "GET",
        url_boards,
        headers=headers,
        params=query
    )
    if (response.status_code < 300):
        print(response.json())
    else:
        print("Request failed")