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


# Headers
headers = {
    "Accept": "application/json"
}

# In order to understand all the methods, you must understand trellos format.
# Each member can have multiple boards. A board can have multiple lists. Each
# list can have multiple cards.

# Gets information on all boards owned by the member.
def get_member_boards(metadata):
    print("Member information")
    
    query = {
        "key": myKey,
        "token": myToken,
    }

    if not metadata:
        query["fields"] = "name,url"

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

# Gets all the lists on a specific board.
def get_lists_on_board(board_id):
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

# Gets all the cards on a board.
def get_cards_on_board(metadata):
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
        if metadata:
            return json
        else:
            cards = []
            for card in json:
                card_information = {
                    "id": card["id"],
                    "name": card["name"]
                }
                cards.append(card_information)
            return cards
    else:
        print("Request failed")
        return "Request failed"