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

# In order to understand all the methods, you must understand trello's format.
# Each member can have multiple boards. A board can have multiple lists. Each
# list can have many cards.

# Get's all the board information with their respective metadata.
def getMemberBoardMetadata():
    print("Member information")

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

# Gets the name of every board owned by member.
def memberBoardsNames():
    print("Board Names")

    # Fields can be added to queries
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

# Gets all the cards on a board but only prints each cards' name.
def getCardsOnBoard():
    print("Gets all cards in a board")

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

    if (response.status_code < 300):
        #TODO: Use the card indexes to do something print the cards in some way with the list name.
        for card in json:
            print(card["name"])
    else:
        print("Request failed")

# Gets all the lists on a board.
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

    if (response.status_code < 300):
        print(json)
    else:
        print("Request failed")