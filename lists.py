import requests
import secrets

# Constants
myKey = secrets.TRELLO_KEY
myToken = secrets.TRELLO_TOKEN
list_id = secrets.SAMPLE_LIST_ID

# URLs
url_list_cards = "https://api.trello.com/1/lists/{list_id}/cards".format(list_id = list_id)


# Headers
headers = {
    "Accept": "application/json"
}

# TODO: add flag for if we want metadata
# Returns all the cards on a specific list.
def get_cards_on_list(list_id):
    print("Cards on List")

    query = {
        "key": myKey,
        "token": myToken,
    }

    response = None
    if (list_id is None):
        response = requests.request(
            "GET",
            url_list_cards,
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