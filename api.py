import requests
import secrets

# Constants
myKey = secrets.TRELLO_KEY
myToken = secrets.TRELLO_TOKEN
member_id = secrets.MEMBER_ID
board_id = secrets.SAMPLE_BOARD_ID
list_id = secrets.SAMPLE_LIST_ID

# URLs
url_boards = "https://api.trello.com/1/members/{member_id}/boards".format(member_id = member_id) # Get information about all boards belonging to member_id
url_board_lists = "https://api.trello.com/1/boards/{board_id}/lists".format(board_id = board_id)
url_board_cards = "https://api.trello.com/1/boards/{board_id}/cards".format(board_id = board_id)
url_list_cards = "https://api.trello.com/1/lists/{list_id}/cards".format(list_id = list_id)


# Headers
headers = {
    "Accept": "application/json"
}

# In order to understand all the methods, you must understand trellos format.
# Each member can have multiple boards. A board can have multiple lists. Each
# list can have multiple cards.

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

    json = response.json()

    if (response.status_code < 300):
        print(json)
    else:
        print("Request failed")
    return json

# Gets the name of every board owned by member.
def getMemberBoardsNames():
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

    json = response.json()

    if (response.status_code < 300):
        print(json)
    else:
        print("Request failed")
    return json

# Gets all the lists on a board.
def getListsOnBoard(board_id):
    print("Lists on board")

    query = {
        "key": myKey,
        "token": myToken,
    }

    response = None
    if (board_id is None):
        response = requests.request(
            "GET",
            url_board_lists,
            headers=headers,
            params=query
        )
    else:
        url = "https://api.trello.com/1/boards/{board_id}/lists".format(board_id = board_id)
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

    json = response.json()

    if (response.status_code < 300):
        for list in json:
            print(list["name"])
    else:
        print("Request failed")
    return json

def getCardsOnList(list_id):
    print("Cards on List")

    query = {
        "key": myKey,
        "token": myToken,
    }

    response = None
    if (board_id is None):
        response = requests.request(
            "GET",
            url_board_lists,
            headers=headers,
            params=query
        )
    else:
        url = "https://api.trello.com/1/lists/{list_id}/cards".format(list_id = list_id)
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

    json = response.json()

    if (response.status_code < 300):
        for card in json:
            print(card["name"])
    else:
        print("Request failed")
    return json

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
    return json

# Gets the cards on a board with all their metadata.
def getCardsWithMetadataOnBoard():
    #FIXME: Implement flag for same method with different information required?
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
        print(json[7])
    else:
        print("Request failed")
    return json

# Gets all the lists on a board and cards on each list and prints them.
def getListsAndCardsOnBoard():
    #TODO: Implement method.

    # Change other methods to return instead of simply print.
    # Create a method that gets the cards metadata as well.
    # Use metadata of cards and information from lists on board
    # to figure out which card belongs to which list.
    # Can use index of each card for this portion.

    # can use each cards section: 
    # card["idList"]
    pass