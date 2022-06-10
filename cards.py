import requests
import secrets

# Constants
myKey = secrets.TRELLO_KEY
myToken = secrets.TRELLO_TOKEN
member_id = secrets.MEMBER_ID
board_id = secrets.SAMPLE_BOARD_ID
list_id = secrets.SAMPLE_LIST_ID

# URLs

# Headers
headers = {
    "Accept": "application/json"
}