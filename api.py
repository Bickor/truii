import requests
import secrets

# Constants
myKey = secrets.TRELLO_KEY
myToken = secrets.TRELLO_TOKEN
member_id = secrets.MEMBER_ID
board_id = secrets.SAMPLE_BOARD_ID

# URLs
url_boards = "https://api.trello.com/1/members/{member_id}/boards".format(member_id = member_id) # Get information about all boards belonging to member_id
url_board_cards = "https://api.trello.com/1/boards/{board_id}/cards".format(board_id = board_id)
url_board_lists = "https://api.trello.com/1/boards/{board_id}/lists".format(board_id = board_id)

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
    print("Board Names")
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

def getBoard():
    query = {
        "key": myKey,
        "token": myToken,
    }

    response = requests.request(
        "GET",
        url_board_cards,
        headers=headers,
        params=query
    )
    json = response.json()

    # TODO: Can also get board index and card index here.
    if (response.status_code < 300):
        for card in json:
            print(card["name"])
    else:
        print("Request failed")

def getListsOnBoard():
    query = {
        "key": myKey,
        "token": myToken,
    }

    response = requests.request(
        "GET",
        url_board_lists,
        headers=headers,
        params=query
    )
    json = response.json()

    # TODO: Can also get board index and card index here.
    if (response.status_code < 300):
        print(json)
    else:
        print("Request failed")